# master search — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `master_search.yaml`, in that flow's own step order, each
followed by its Mermaid `sequenceDiagram`.

## search_1

```mermaid
sequenceDiagram
  title Business Loan Discovery (via ONDC Tunnel)
  participant Borrower Platform (BAP)
  participant ONDC Tunnel
  participant Lender Platform(BPP)
  rect rgb(191, 223, 255)
  Borrower Platform (BAP)->>ONDC Tunnel: search
  Note over ONDC Tunnel: Schema validation
  alt Payload fails validation
    ONDC Tunnel-->>Borrower Platform (BAP): NACK with error (reaches no lender, retryable)
  else Payload valid
    ONDC Tunnel->>Borrower Platform (BAP): ACK
    Note over ONDC Tunnel: Forward only to lenders whose portal declarations permit this BAP
    ONDC Tunnel->>Lender Platform(BPP): search
    Lender Platform(BPP)->>ONDC Tunnel: ACK
  end
  end
  Lender Platform(BPP)->>ONDC Tunnel: Publish Catalog of Lender 1 (on_search)
  ONDC Tunnel->>Borrower Platform (BAP): Publish Catalog of Lender 1 (on_search)
  Borrower Platform (BAP)->>ONDC Tunnel: ACK
  ONDC Tunnel->>Lender Platform(BPP): ACK
```

## on_Search_1

```mermaid
sequenceDiagram
  title Business Loan Discovery (via ONDC Tunnel)
  participant Borrower Platform (BAP)
  participant ONDC Tunnel
  participant Lender Platform(BPP)
  Borrower Platform (BAP)->>ONDC Tunnel: search
  ONDC Tunnel->>Borrower Platform (BAP): ACK
  ONDC Tunnel->>Lender Platform(BPP): search
  Lender Platform(BPP)->>ONDC Tunnel: ACK
  rect rgb(191, 223, 255)
  Lender Platform(BPP)->>ONDC Tunnel: Publish Catalog of Lender 1 (on_search)
  Note over ONDC Tunnel: Schema validation
  alt Catalog fails validation
    ONDC Tunnel-->>Lender Platform(BPP): NACK with error (catalog not delivered to BAP)
  else Catalog valid
    ONDC Tunnel->>Borrower Platform (BAP): Publish Catalog of Lender 1 (on_search)
    Borrower Platform (BAP)->>ONDC Tunnel: ACK
    ONDC Tunnel->>Lender Platform(BPP): ACK
  end
  end
```
