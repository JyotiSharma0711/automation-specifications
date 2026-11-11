# lamf credit line drawdown with mfc single redirection — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `lamf_credit_line_drawdown_with_mfc_single_redirection.yaml`, in that flow's own step order, each
followed by its Mermaid `sequenceDiagram`.

## init_1

```mermaid
sequenceDiagram
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  rect rgb(191, 223, 255)
  Borrower Platform (BAP)->>Lender Platform (BPP): init-Request (DRAWDOWN on Base Order)
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
  end
  Lender Platform (BPP)->>Borrower Platform (BAP): on_init - Approved drawdown terms and consent required
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
```

## on_init_1

```mermaid
sequenceDiagram
 participant Borrower Platform (BAP)
 participant Lender Platform (BPP)
 
 Borrower Platform (BAP)->>Lender Platform (BPP): init-Request (DRAWDOWN on Base Order)
 Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
 rect rgb(191, 223, 255)
 Lender Platform (BPP)->>Borrower Platform (BAP): on_init - Approved drawdown terms and consent required
 Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
 end
```

## confirm_1

```mermaid
sequenceDiagram
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  rect rgb(191, 223, 255)
  Borrower Platform (BAP)->>Lender Platform (BPP): confirm
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
  end
  Lender Platform (BPP)->>Borrower Platform (BAP): on_confirm
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
```

## on_confirm_1

```mermaid
sequenceDiagram
 participant Borrower Platform (BAP)
 participant Lender Platform (BPP)
 
 Borrower Platform (BAP)->>Lender Platform (BPP): confirm
 Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
 rect rgb(191, 223, 255)
 Lender Platform (BPP)->>Borrower Platform (BAP): on_confirm
 Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
 end
```

## on_update_1

```mermaid
sequenceDiagram
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  rect rgb(191, 223, 255)
  Lender Platform (BPP)->>Borrower Platform (BAP): on_update - Child Order
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  end
  Lender Platform (BPP)->>Borrower Platform (BAP): on_update - Base Order
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
```

## on_update_2

```mermaid
sequenceDiagram
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  
  Lender Platform (BPP)->>Borrower Platform (BAP): on_update - Child Order
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  rect rgb(191, 223, 255)
  Lender Platform (BPP)->>Borrower Platform (BAP): on_update - Base Order
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  end
```
