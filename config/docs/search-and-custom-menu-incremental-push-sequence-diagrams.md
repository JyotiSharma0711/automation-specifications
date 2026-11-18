# Search and Custom Menu (Incremental Push) — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Search_and_Custom_Menu_(Incremental_Push).yaml`, in that flow's own step order, each
followed by its Mermaid `sequenceDiagram`. Derived by splitting the matching flow in this branch's own `flow-diagrams.md` (one combined diagram per whole flow) into one small diagram per individual API call, highlighting that call's own message(s) — same convention as the other domains' per-step sequence-diagram docs.

## search_inc

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Gateway: /search (start incremental session)
  Gateway->>Seller App (BPP): /search (forwarded)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): changed items
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): store closed
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): store open
  Buyer App (BAP)->>Gateway: /search (follow-up sync)
  Gateway->>Seller App (BPP): /search (forwarded)
```

## on_search_inc

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (start incremental session)
  Gateway->>Seller App (BPP): /search (forwarded)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): changed items
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): store closed
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): store open
  Buyer App (BAP)->>Gateway: /search (follow-up sync)
  Gateway->>Seller App (BPP): /search (forwarded)
```

## on_search_inc_close

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (start incremental session)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): changed items
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): store closed
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): store open
  Buyer App (BAP)->>Gateway: /search (follow-up sync)
  Gateway->>Seller App (BPP): /search (forwarded)
```

## on_search_inc_open

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (start incremental session)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): changed items
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): store closed
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): store open
  end
  Buyer App (BAP)->>Gateway: /search (follow-up sync)
  Gateway->>Seller App (BPP): /search (forwarded)
```

## search_inc1

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Gateway
  participant Seller App (BPP)
  Buyer App (BAP)->>Gateway: /search (start incremental session)
  Gateway->>Seller App (BPP): /search (forwarded)
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): changed items
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): store closed
  Seller App (BPP)-->>Buyer App (BAP): /on_search (unsolicited): store open
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Gateway: /search (follow-up sync)
  Gateway->>Seller App (BPP): /search (forwarded)
  end
```
