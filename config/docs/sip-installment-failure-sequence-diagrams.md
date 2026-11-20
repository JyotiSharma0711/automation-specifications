# SIP Installment Failure — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `SIP_Installment_Failure.yaml`, in that flow's own step order, each
followed by its Mermaid `sequenceDiagram`.

on_update_unsolicited_installment_failure has no clean dedicated source (the WIP source repo's own "payment failure" step mislabels an on_confirm diagram, not an actual failure message) -- reuses the generic unsolicited on_update diagram instead.

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

## on_select_1

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

## investor_details_form

```mermaid
sequenceDiagram
  participant Buyer Platform (BAP)
  participant Seller Platform (BPP)
  participant Seller Form Service
  rect rgb(191, 223, 255)
  Buyer Platform (BAP)->> Seller Form Service: Get Form
  Seller Form Service-->>Buyer Platform (BAP): Form Received
  Buyer Platform (BAP)->>Seller Form Service: Form Submission
  Seller Form Service-->>Buyer Platform (BAP): Submission ID   
  end
  Buyer Platform (BAP)->>Seller Platform (BPP): select
  Seller Platform (BPP)-->>Buyer Platform (BAP):ACK
  Seller Platform (BPP)->>Buyer Platform (BAP):on_select
  Buyer Platform (BAP)-->>Seller Platform (BPP): ACK
  
```

## select_2

```mermaid
sequenceDiagram
  participant Buyer Platform (BAP)
  participant Seller Platform (BPP)
  participant Seller Form Service
  
  Buyer Platform (BAP)->> Seller Form Service: Get Form
  Seller Form Service-->>Buyer Platform (BAP): Form Received
  Buyer Platform (BAP)->>Seller Form Service: Form Submission
  Seller Form Service-->>Buyer Platform (BAP): Submission ID   
  rect rgb(191, 223, 255)
  Buyer Platform (BAP)->>Seller Platform (BPP): select
  Seller Platform (BPP)-->>Buyer Platform (BAP):ACK
  end
  Seller Platform (BPP)->>Buyer Platform (BAP):on_select
  Buyer Platform (BAP)-->>Seller Platform (BPP): ACK
```

## on_select_2

```mermaid
sequenceDiagram
  participant Buyer Platform (BAP)
  participant Seller Platform (BPP)
  participant Seller Form Service
  
  Buyer Platform (BAP)->> Seller Form Service: Get Form
  Seller Form Service-->>Buyer Platform (BAP): Form Received
  Buyer Platform (BAP)->>Seller Form Service: Form Submission
  Seller Form Service-->>Buyer Platform (BAP): Submission ID   
  Buyer Platform (BAP)->>Seller Platform (BPP): select
  Seller Platform (BPP)-->>Buyer Platform (BAP):ACK
  rect rgb(191, 223, 255)
  Seller Platform (BPP)->>Buyer Platform (BAP):on_select
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
  Seller Platform (BPP)->>Buyer Platform (BAP):on_init
  Buyer Platform (BAP)-->>Seller Platform (BPP): ACK
  
```

## on_init

```mermaid
sequenceDiagram
  participant Buyer Platform (BAP)
  participant Seller Platform (BPP)
  Buyer Platform (BAP)->>Seller Platform (BPP): init
  Seller Platform (BPP)-->>Buyer Platform (BAP):ACK
  rect rgb(191, 223, 255)
  Seller Platform (BPP)->>Buyer Platform (BAP):on_init
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
  Seller Platform (BPP)->>Buyer Platform (BAP):on_confirm
  Buyer Platform (BAP)-->>Seller Platform (BPP): ACK
  
```

## on_confirm

```mermaid
sequenceDiagram
  participant Buyer Platform (BAP)
  participant Seller Platform (BPP)
  Buyer Platform (BAP)->>Seller Platform (BPP): confirm
  Seller Platform (BPP)-->>Buyer Platform (BAP):ACK
  rect rgb(191, 223, 255)
  Seller Platform (BPP)->>Buyer Platform (BAP):on_confirm
  Buyer Platform (BAP)-->>Seller Platform (BPP): ACK
  end
```

## on_update_unsolicited_installment_failure

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

## on_status_unsolicited_payment

```mermaid
sequenceDiagram
  participant Buyer Platform (BAP)
  participant Seller Platform (BPP)
  rect rgb(191, 223, 255)
  Buyer Platform (BAP)->>Seller Platform (BPP): on_status
  Seller Platform (BPP)-->>Buyer Platform (BAP):ACK
  end
  Seller Platform (BPP)->>Buyer Platform (BAP):on_update
  Buyer Platform (BAP)-->>Seller Platform (BPP): ACK
  
```

## on_update_unsolicited

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
