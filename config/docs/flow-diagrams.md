# Flow Diagrams (ONDC:RET10 1.2.0)

Sequence diagrams for each flow in this specification. Solid arrows are requests; dashed arrows are callbacks (`on_*`). **(unsolicited)** marks a message the sender pushes on its own, not as a reply to a request.

To keep the diagrams short, flows that start with a normal order show those steps as a single note. The full order steps are in Flow 1.

---

## Order Lifecycle at a Glance

```mermaid
flowchart LR
    A[Discovery<br/>search / on_search] --> B[Quote<br/>select / on_select]
    B --> C[Initialize<br/>init / on_init]
    C --> D[Confirm<br/>confirm / on_confirm]
    D --> E[Fulfillment<br/>on_status, track]
    E --> F[Delivered]
    D -. buyer cancels .-> G[Cancelled<br/>cancel / on_cancel]
    D -. seller part-cancels .-> H[Part-cancelled<br/>on_update]
    E -. delivery fails .-> I[RTO<br/>on_cancel]
    F -. buyer returns .-> J[Return<br/>update / on_update]
    F -. buyer complains .-> K[Grievance<br/>issue / on_issue]
```

---

## Flow 1: Delivery Flow

The standard order: the buyer selects items, gets a quote, pays online, and receives the order through seller-managed delivery.

```mermaid
sequenceDiagram
    participant BAP as Buyer App (BAP)
    participant BPP as Seller App (BPP)
    BAP->>BPP: /select (items, store, delivery location)
    BPP-->>BAP: /on_select (quote, TAT)
    BAP->>BPP: /init (address, billing)
    BPP-->>BAP: /on_init (final quote, payment terms)
    BAP->>BPP: /confirm (payment PAID)
    BPP-->>BAP: /on_confirm (order Created)
    BPP-->>BAP: /on_status (unsolicited): Accepted
    BPP-->>BAP: /on_status (unsolicited): Packed
    BPP-->>BAP: /on_status (unsolicited): Agent-assigned
    BPP-->>BAP: /on_status (unsolicited): Order-picked-up
    BAP->>BPP: /track
    BPP-->>BAP: /on_track (live tracking)
    BPP-->>BAP: /on_status (unsolicited): Out-for-delivery
    BPP-->>BAP: /on_status (unsolicited): Order-delivered
```

---

## Flow 2: Buyer Delivery Flow

The buyer app arranges delivery. The seller packs the order, and the buyer app reports delivery progress back to the seller.

```mermaid
sequenceDiagram
    participant BAP as Buyer App (BAP)
    participant BPP as Seller App (BPP)
    Note over BAP,BPP: /select → /on_confirm (as in Flow 1)
    BPP-->>BAP: /on_status (unsolicited): Pending
    BPP-->>BAP: /on_status (unsolicited): Packed
    BAP->>BPP: /update (interim delivery update)
    BPP-->>BAP: /on_update (acknowledged)
    BAP->>BPP: /update (order delivered by buyer's courier)
    BPP-->>BAP: /on_update (order completed)
```

---

## Flow 3: Out of Stock Flow (Error Code)

The seller rejects the first selection because an item is out of stock. The buyer corrects the cart and completes the order.

```mermaid
sequenceDiagram
    participant BAP as Buyer App (BAP)
    participant BPP as Seller App (BPP)
    BAP->>BPP: /select (original cart)
    BPP-->>BAP: /on_select (error 40002: item out of stock)
    BAP->>BPP: /select (corrected cart)
    BPP-->>BAP: /on_select (quote)
    BAP->>BPP: /init
    BPP-->>BAP: /on_init
    BAP->>BPP: /confirm
    BPP-->>BAP: /on_confirm
    Note over BAP,BPP: Fulfillment and delivery as in Flow 1
```

---

## Flow 4: Buyer Cancellation Flow

The buyer cancels a confirmed order before it is shipped.

```mermaid
sequenceDiagram
    participant BAP as Buyer App (BAP)
    participant BPP as Seller App (BPP)
    Note over BAP,BPP: /select → /on_confirm (as in Flow 1)
    BAP->>BPP: /cancel (order ID, reason code)
    BPP-->>BAP: /on_cancel (Cancelled, charges and refund)
```

---

## Flow 5: RTO and Part-Cancellation Flow

The seller cancels some items it cannot supply, then delivery of the rest fails and the order returns to the seller (Return to Origin).

```mermaid
sequenceDiagram
    participant BAP as Buyer App (BAP)
    participant BPP as Seller App (BPP)
    Note over BAP,BPP: /select → /on_confirm (as in Flow 1)
    BPP-->>BAP: /on_update (unsolicited): part-cancel unavailable items
    BAP->>BPP: /update (settlement for refund)
    BPP-->>BAP: /on_status (unsolicited): Packed
    BPP-->>BAP: /on_status (unsolicited): Agent-assigned
    BPP-->>BAP: /on_status (unsolicited): Order-picked-up
    BPP-->>BAP: /on_status (unsolicited): Out-for-delivery
    BPP-->>BAP: /on_cancel (unsolicited): RTO, reason code 013
    BAP->>BPP: /update (settlement for refund)
    BPP-->>BAP: /on_status (unsolicited): RTO-Delivered
```

---

## Flow 6: Return Flow

After delivery, the buyer returns an item. The seller approves the return, the item is picked up, and the refund is settled.

```mermaid
sequenceDiagram
    participant BAP as Buyer App (BAP)
    participant BPP as Seller App (BPP)
    Note over BAP,BPP: /select → Order-delivered (as in Flow 1, without /track)
    BAP->>BPP: /update (return request: item, quantity, reason)
    BPP-->>BAP: /on_update (return initiated)
    BPP-->>BAP: /on_update (unsolicited): return approved
    BPP-->>BAP: /on_update (unsolicited): return picked up
    BAP->>BPP: /update (settlement for refund)
    BPP-->>BAP: /on_update (unsolicited): return delivered to seller
```

---

## Flow 7: Discovery Flow – Full Catalog

The buyer app searches a city and the seller returns its full catalog.

```mermaid
sequenceDiagram
    participant BAP as Buyer App (BAP)
    participant GW as Gateway
    participant BPP as Seller App (BPP)
    BAP->>GW: /search (city, domain)
    GW->>BPP: /search (forwarded)
    BPP-->>BAP: /on_search (full catalog)
```

---

## Flow 8: Discovery Flow – Incremental Catalog (Push)

After the first search, the seller pushes catalog changes as they happen, without resending the whole catalog.

```mermaid
sequenceDiagram
    participant BAP as Buyer App (BAP)
    participant GW as Gateway
    participant BPP as Seller App (BPP)
    BAP->>GW: /search (start incremental session)
    GW->>BPP: /search (forwarded)
    BPP-->>BAP: /on_search (unsolicited): changed items
    BPP-->>BAP: /on_search (unsolicited): store closed
    BPP-->>BAP: /on_search (unsolicited): store open
    BAP->>GW: /search (follow-up sync)
    GW->>BPP: /search (forwarded)
```

---

## Flow 9: Discovery Flow – Incremental Catalog Refresh (Pull)

The buyer app asks the seller for only the items that changed after a given time.

```mermaid
sequenceDiagram
    participant BAP as Buyer App (BAP)
    participant GW as Gateway
    participant BPP as Seller App (BPP)
    BAP->>GW: /search (city, domain)
    GW->>BPP: /search (forwarded)
    BPP-->>BAP: /on_search (full catalog)
    BAP->>BPP: /search (items changed after a given time)
    BPP-->>BAP: /on_search (changed items only)
```

---

## Flow 10: Catalog Rejection Flow

The buyer app finds errors in a seller's catalog and rejects it, telling the seller what is wrong.

```mermaid
sequenceDiagram
    participant BAP as Buyer App (BAP)
    participant GW as Gateway
    participant BPP as Seller App (BPP)
    BAP->>GW: /search (city, domain)
    GW->>BPP: /search (forwarded)
    BPP-->>BAP: /on_search (catalog)
    BAP->>BPP: /catalog_rejection (error type, code, message, path)
```

---

## Flow 11: Delivery Flow with IGM 1.0.0

A delivered order followed by a complaint handled under IGM 1.0.0.

```mermaid
sequenceDiagram
    participant BAP as Buyer App (BAP)
    participant BPP as Seller App (BPP)
    Note over BAP,BPP: /select → Order-delivered (as in Flow 1)
    BAP->>BPP: /issue (open complaint)
    BPP-->>BAP: /on_issue (processing)
    BPP-->>BAP: /on_issue_status (unsolicited): resolution
    BAP->>BPP: /issue (close)
```

---

## Flow 12: Delivery Flow with IGM 2.0.0 – No Action

The seller resolves the complaint with an explanation and no further action, and the buyer accepts.

```mermaid
sequenceDiagram
    participant BAP as Buyer App (BAP)
    participant BPP as Seller App (BPP)
    Note over BAP,BPP: /select → Order-delivered (as in Flow 1)
    BAP->>BPP: /issue (open complaint)
    BPP-->>BAP: /on_issue (processing)
    BPP-->>BAP: /on_issue (unsolicited): resolution, no action
    BAP->>BPP: /issue (accept resolution)
    BPP-->>BAP: /on_issue (resolved)
    BAP->>BPP: /issue (close)
    BPP-->>BAP: /on_status (unsolicited): final order status
```

---

## Flow 13: Delivery Flow with IGM 2.0.0 – Rejection and Escalation

The buyer rejects the seller's resolution and escalates the complaint. The final resolution leads to a return.

```mermaid
sequenceDiagram
    participant BAP as Buyer App (BAP)
    participant BPP as Seller App (BPP)
    Note over BAP,BPP: /select → Order-delivered (as in Flow 1)
    BAP->>BPP: /issue (open complaint)
    BPP-->>BAP: /on_issue (processing)
    BPP-->>BAP: /on_issue (unsolicited): resolution
    BAP->>BPP: /issue (reject resolution)
    BPP-->>BAP: /on_issue (reprocessing)
    BPP-->>BAP: /on_issue (unsolicited): new resolution
    BAP->>BPP: /issue (escalate)
    BPP-->>BAP: /on_issue (escalation processing)
    BPP-->>BAP: /on_issue (unsolicited): final resolution
    BAP->>BPP: /issue (accept resolution)
    BPP-->>BAP: /on_issue (resolved)
    BAP->>BPP: /issue (close)
    BPP-->>BAP: /on_update (unsolicited): return started on the order
```

---

## Flow 14: Delivery Flow with IGM 2.0.0

The seller asks for more information, proposes a replacement, and the buyer accepts.

```mermaid
sequenceDiagram
    participant BAP as Buyer App (BAP)
    participant BPP as Seller App (BPP)
    Note over BAP,BPP: /select → Order-delivered (as in Flow 1)
    BAP->>BPP: /issue (open complaint)
    BPP-->>BAP: /on_issue (processing)
    BPP-->>BAP: /on_issue (unsolicited): need more information
    BAP->>BPP: /issue (information provided)
    BPP-->>BAP: /on_issue (information acknowledged)
    BPP-->>BAP: /on_issue (unsolicited): resolution
    BAP->>BPP: /issue (accept resolution)
    BPP-->>BAP: /on_issue (resolved)
    BAP->>BPP: /issue (close)
    BPP-->>BAP: /on_update (unsolicited): replacement started on the order
```
