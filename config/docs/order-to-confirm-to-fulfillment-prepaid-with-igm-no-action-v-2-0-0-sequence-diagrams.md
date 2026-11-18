# Order to confirm to fulfillment  Prepaid with IGM No Action v-2.0.0 — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Order_to_confirm_to_fulfillment__Prepaid_with_IGM_No_Action_v-2.0.0.yaml`, in that flow's own step order, each
followed by its Mermaid `sequenceDiagram`. Derived by splitting the matching flow in this branch's own `flow-diagrams.md` (one combined diagram per whole flow) into one small diagram per individual API call, highlighting that call's own message(s) — same convention as the other domains' per-step sequence-diagram docs.

## select

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Buyer App (BAP)->>Seller App (BPP): /track
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## on_select

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  end
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Buyer App (BAP)->>Seller App (BPP): /track
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## init

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Buyer App (BAP)->>Seller App (BPP): /track
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## on_init

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  end
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Buyer App (BAP)->>Seller App (BPP): /track
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## confirm

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Buyer App (BAP)->>Seller App (BPP): /track
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## on_confirm

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Buyer App (BAP)->>Seller App (BPP): /track
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## on_status_accepted

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Buyer App (BAP)->>Seller App (BPP): /track
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## on_status_packed

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Buyer App (BAP)->>Seller App (BPP): /track
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## on_status_agent_assigned

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Buyer App (BAP)->>Seller App (BPP): /track
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## on_status_picked

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  end
  Buyer App (BAP)->>Seller App (BPP): /track
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## track

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /track
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## on_track

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Buyer App (BAP)->>Seller App (BPP): /track
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## on_status_out_for_delivery

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Buyer App (BAP)->>Seller App (BPP): /track
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## on_status_order_delivered

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Buyer App (BAP)->>Seller App (BPP): /track
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## issue_open_2

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Buyer App (BAP)->>Seller App (BPP): /track
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## on_issue_processing

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Buyer App (BAP)->>Seller App (BPP): /track
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## on_issue_resolution_igm_3

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Buyer App (BAP)->>Seller App (BPP): /track
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## issue_resolution_accept_igm_3

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Buyer App (BAP)->>Seller App (BPP): /track
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## on_issue_resolved_igm_3

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Buyer App (BAP)->>Seller App (BPP): /track
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  end
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## issue_close_igm_3

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Buyer App (BAP)->>Seller App (BPP): /track
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  rect rgb(191, 223, 255)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  end
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
```

## on_status_igm_3

```mermaid
sequenceDiagram
  participant Buyer App (BAP)
  participant Seller App (BPP)
  Buyer App (BAP)->>Seller App (BPP): /select (items, store, delivery location)
  Seller App (BPP)-->>Buyer App (BAP): /on_select (quote, TAT)
  Buyer App (BAP)->>Seller App (BPP): /init (address, billing)
  Seller App (BPP)-->>Buyer App (BAP): /on_init (final quote, payment terms)
  Buyer App (BAP)->>Seller App (BPP): /confirm (payment PAID)
  Seller App (BPP)-->>Buyer App (BAP): /on_confirm (order Created)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Accepted
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Packed
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Agent-assigned
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-picked-up
  Buyer App (BAP)->>Seller App (BPP): /track
  Seller App (BPP)-->>Buyer App (BAP): /on_track (live tracking)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Out-for-delivery
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): Order-delivered
  Buyer App (BAP)->>Seller App (BPP): /issue (open complaint)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (processing)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (unsolicited): resolution, no action
  Buyer App (BAP)->>Seller App (BPP): /issue (accept resolution)
  Seller App (BPP)-->>Buyer App (BAP): /on_issue (resolved)
  Buyer App (BAP)->>Seller App (BPP): /issue (close)
  rect rgb(191, 223, 255)
  Seller App (BPP)-->>Buyer App (BAP): /on_status (unsolicited): final order status
  end
```
