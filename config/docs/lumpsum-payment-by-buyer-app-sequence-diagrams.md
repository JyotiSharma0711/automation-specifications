# Lumpsum Payment By Buyer App — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Lumpsum_Payment_By_Buyer_App.yaml`, in that flow's own step order, each
followed by its Mermaid `sequenceDiagram`.

update_buyer_payment/on_update_buyer_payment have no dedicated source (the buyer app reports its own payment completion instead of going through a payment-gateway redirection form); reuse the generic update/on_update pair (same role: a buyer-initiated status report, acknowledged by the seller).

## select

```mermaid
sequenceDiagram
  participant Buyer Platform (BAP)
  participant Seller Platform (BPP)
  rect rgb(191, 223, 255)
  Buyer Platform (BAP)->>Seller Platform (BPP): select
  Seller Platform (BPP)-->>Buyer Platform (BAP):ACK
  end
  Seller Platform (BPP)->>Buyer Platform (BAP): on_select
  Buyer Platform (BAP)-->>Seller Platform (BPP): ACK
```

## on_select_existing_folio

```mermaid
sequenceDiagram
  participant Buyer Platform (BAP)
  participant Seller Platform (BPP)
  
  Buyer Platform (BAP)->>Seller Platform (BPP): select
  Seller Platform (BPP)-->>Buyer Platform (BAP):ACK
  rect rgb(191, 223, 255)
  Seller Platform (BPP)->>Buyer Platform (BAP): on_select
  Buyer Platform (BAP)-->>Seller Platform (BPP): ACK
  end
```

## init

```mermaid
sequenceDiagram
  participant Buyer Platform (BAP)
  participant Seller Platform (BPP)
  rect rgb(191, 223, 255)
  Buyer Platform (BAP)->>Seller Platform (BPP): init
  Seller Platform (BPP)-->>Buyer Platform (BAP):ACK
  end
  Seller Platform (BPP)->>Buyer Platform (BAP): on_init
  Buyer Platform (BAP)-->>Seller Platform (BPP): ACK
  
```

## on_init_existing_folio

```mermaid
sequenceDiagram
  participant Buyer Platform (BAP)
  participant Seller Platform (BPP)
  
  Buyer Platform (BAP)->>Seller Platform (BPP): init
  Seller Platform (BPP)-->>Buyer Platform (BAP):ACK
  rect rgb(191, 223, 255)
  Seller Platform (BPP)->>Buyer Platform (BAP): on_init
  Buyer Platform (BAP)-->>Seller Platform (BPP): ACK
  end
```

## confirm

```mermaid
sequenceDiagram
  participant Buyer Platform (BAP)
  participant Seller Platform (BPP)
  rect rgb(191, 223, 255)
  Buyer Platform (BAP)->>Seller Platform (BPP): confirm
  Seller Platform (BPP)-->>Buyer Platform (BAP):ACK
  end
  Seller Platform (BPP)->>Buyer Platform (BAP): on_confirm
  Buyer Platform (BAP)-->>Seller Platform (BPP): ACK
```

## on_confirm_existing_folio

```mermaid
sequenceDiagram
  participant Buyer Platform (BAP)
  participant Seller Platform (BPP)
  
  Buyer Platform (BAP)->>Seller Platform (BPP): confirm
  Seller Platform (BPP)-->>Buyer Platform (BAP):ACK
  rect rgb(191, 223, 255)
  Seller Platform (BPP)->>Buyer Platform (BAP): on_confirm
  Buyer Platform (BAP)-->>Seller Platform (BPP): ACK
  end
```

## update_buyer_payment

```mermaid
sequenceDiagram
  participant Buyer Platform (BAP)
  participant Seller Platform (BPP)
  rect rgb(191, 223, 255)
  Buyer Platform (BAP)->>Seller Platform (BPP): update
  Seller Platform (BPP)-->>Buyer Platform (BAP):ACK
  end
  Seller Platform (BPP)->>Buyer Platform (BAP):on_update
  Buyer Platform (BAP)-->>Seller Platform (BPP): ACK
  
```

## on_update_buyer_payment

```mermaid
sequenceDiagram
  participant Buyer Platform (BAP)
  participant Seller Platform (BPP)
  Buyer Platform (BAP)->>Seller Platform (BPP): update
  Seller Platform (BPP)-->>Buyer Platform (BAP):ACK
  rect rgb(191, 223, 255)
  Seller Platform (BPP)->>Buyer Platform (BAP):on_update
  Buyer Platform (BAP)-->>Seller Platform (BPP): ACK
  end
```

## on_update_unsolicited_existing_folio

```mermaid
sequenceDiagram
  participant Buyer Platform (BAP)
  participant Seller Platform (BPP)
  Buyer Platform (BAP)->>Seller Platform (BPP): on_status
  Seller Platform (BPP)-->>Buyer Platform (BAP):ACK
  rect rgb(191, 223, 255)
  Seller Platform (BPP)->>Buyer Platform (BAP):on_update
  Buyer Platform (BAP)-->>Seller Platform (BPP): ACK
  end
```
