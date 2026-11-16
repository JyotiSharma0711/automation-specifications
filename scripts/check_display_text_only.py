#!/usr/bin/env python3
"""
Guardrail for config/flows/index.yaml: fails if a diff changes anything
other than an allow-listed, free-text display field.

Usage:
    check_display_text_only.py <base_ref> <head_ref> [path_to_index_yaml]

Exit 0 if the only differences between base and head are value changes to
allow-listed text leaves. Exit 1 otherwise, printing every offending path.

Allow-listed leaves (business-team editable, per the journey-display-metadata
skill's schema reference):
  - flows[i].description
  - flows[i].meta.display.actions.<action_id>
  - flows[i].meta.display.sections[j].actions.<action_id>
  - flows[i].meta.display.inline[j].label

Everything else that differs between base and head (added/removed keys,
reordered list items, changed section names, changed after_section/
skip_sections/kind/type/order/preferred/$ref/usecase/tags/action_id keys,
or a value change at any path not on the allow-list above) is a violation.
"""
import sys
import subprocess
import yaml


def load_yaml_at_ref(ref: str, path: str):
    result = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"Could not read {path} at {ref}: {result.stderr.strip()}", file=sys.stderr)
        sys.exit(2)
    return yaml.safe_load(result.stdout)


def is_allowlisted_leaf(path):
    """path is a list of keys/indices from the document root."""
    # flows[i].description
    if len(path) == 3 and path[0] == "flows" and path[2] == "description":
        return True
    # flows[i].meta.display.actions.<id>
    if (
        len(path) == 6
        and path[0] == "flows" and path[2] == "meta"
        and path[3] == "display" and path[4] == "actions"
    ):
        return True
    # flows[i].meta.display.sections[j].actions.<id>
    if (
        len(path) == 8
        and path[0] == "flows" and path[2] == "meta"
        and path[3] == "display" and path[4] == "sections"
        and path[6] == "actions"
    ):
        return True
    # flows[i].meta.display.inline[j].label
    if (
        len(path) == 7
        and path[0] == "flows" and path[2] == "meta"
        and path[3] == "display" and path[4] == "inline"
        and path[6] == "label"
    ):
        return True
    return False


def diff(old, new, path, violations):
    if type(old) != type(new):
        violations.append((path, f"type changed: {type(old).__name__} -> {type(new).__name__}"))
        return

    if isinstance(old, dict):
        old_keys, new_keys = set(old.keys()), set(new.keys())
        if old_keys != new_keys:
            added = new_keys - old_keys
            removed = old_keys - new_keys
            if added:
                violations.append((path, f"key(s) added: {sorted(added)}"))
            if removed:
                violations.append((path, f"key(s) removed: {sorted(removed)}"))
        for key in old_keys & new_keys:
            diff(old[key], new[key], path + [key], violations)
        return

    if isinstance(old, list):
        if len(old) != len(new):
            violations.append((path, f"list length changed: {len(old)} -> {len(new)} (add/remove/reorder not allowed)"))
            return
        for i, (o, n) in enumerate(zip(old, new)):
            diff(o, n, path + [i], violations)
        return

    # scalar leaf
    if old != new:
        if is_allowlisted_leaf(path):
            return  # permitted text edit
        violations.append((path, f"value changed at a non-text-editable field: {old!r} -> {new!r}"))


def format_path(path):
    out = "flows"
    for p in path[1:]:
        out += f"[{p}]" if isinstance(p, int) else f".{p}"
    return out


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    base_ref, head_ref = sys.argv[1], sys.argv[2]
    yaml_path = sys.argv[3] if len(sys.argv) > 3 else "config/flows/index.yaml"

    old_doc = load_yaml_at_ref(base_ref, yaml_path)
    new_doc = load_yaml_at_ref(head_ref, yaml_path)

    violations = []
    diff(old_doc, new_doc, [], violations)

    if violations:
        print(f"BLOCKED: {len(violations)} non-text-only change(s) to {yaml_path}:\n")
        for path, reason in violations:
            print(f"  - {format_path(path)}: {reason}")
        print(
            "\nOnly these fields may change via this guardrail: flow-level "
            "`description`, meta.display.actions.<id>, "
            "meta.display.sections[].actions.<id>, and meta.display.inline[].label. "
            "Anything else (structure, ordering, section names, inline wiring, meta "
            "fields) needs an engineering PR. See the journey-display-metadata skill."
        )
        sys.exit(1)

    print(f"OK: only allow-listed text fields changed in {yaml_path}.")
    sys.exit(0)


if __name__ == "__main__":
    main()
