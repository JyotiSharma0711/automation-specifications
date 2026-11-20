# Search Incremental Pull — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `Search_Incremental_Pull.yaml`, in that flow's own step order, each
followed by its Mermaid `sequenceDiagram`.

## search_incremental_pull

```mermaid
sequenceDiagram
  rect rgb(191, 223, 255)
  Buyer Platform (BAP)->>Gateway (BG): search
  Gateway (BG) ->> Buyer Platform (BAP): ACK
  Gateway (BG)->>Registry: Lookup Seller Platforms (lookup)
  Registry->>Gateway (BG): List of Seller Platforms (200 OK)
  Gateway (BG)->>Seller Platform (BPP): search
  Seller Platform (BPP)->>Gateway (BG) : ACK
  end
  Seller Platform (BPP)->>Buyer Platform (BAP): Publish Catalog of Seller 1 (on_search)
  Buyer Platform (BAP)->>Seller Platform (BPP): ACK
  
```

## on_search_incremental_pull

```mermaid
sequenceDiagram
  Buyer Platform (BAP)->>Gateway (BG): search
  Gateway (BG) ->> Buyer Platform (BAP): ACK
  Gateway (BG)->>Registry: Lookup Seller Platforms (lookup)
  Registry->>Gateway (BG): List of Seller Platforms (200 OK)
  Gateway (BG)->>Seller Platform (BPP): search
  Seller Platform (BPP)->>Gateway (BG) : ACK
  rect rgb(191, 223, 255)
  Seller Platform (BPP)->>Buyer Platform (BAP): Publish Catalog of Seller 1 (on_search)
  Buyer Platform (BAP)->>Seller Platform (BPP): ACK
  end
```
