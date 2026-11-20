# SWP by amount — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `SWP_by_amount.yaml.yaml`, in that flow's own step order, each
followed by its Mermaid `sequenceDiagram`.

No dedicated source exists for this step; reuses the generic diagram already established for the same role (select/on_select/init/on_init/confirm/on_confirm/on_status/on_update) elsewhere in this domain's own source material.

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
