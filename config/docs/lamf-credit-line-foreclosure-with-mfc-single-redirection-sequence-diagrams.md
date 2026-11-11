# lamf credit line foreclosure with mfc single redirection — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `lamf_credit_line_foreclosure_with_mfc_single_redirection.yaml`, in that flow's own step order, each
followed by its Mermaid `sequenceDiagram`.

`payment_url_form` has no counterpart in ONDC-FIS-Specifications; reuses the generic payment-redirection diagram already authored for Personal Loan (same `order.payments[0].url` field reference).

## search_1

```mermaid
sequenceDiagram
  title  Personal Loan Discovery
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)

  rect rgb(191, 223, 255) 
  Borrower Platform (BAP)->>Lender Platform (BPP): search
  Lender Platform (BPP)-->>Borrower Platform (BAP):ACK
  end
  Lender Platform (BPP)->>Borrower Platform (BAP):on_on_search
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
```

## on_search_1

```mermaid
sequenceDiagram
  title  Personal Loan Discovery
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  
  Borrower Platform (BAP)->>Lender Platform (BPP): search(with submissionID)
  Lender Platform (BPP)-->>Borrower Platform (BAP):ACK
  rect rgb(191, 223, 255) 
  Lender Platform (BPP)->>Borrower Platform (BAP):on_on_search
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  end
```

## select_1

```mermaid
sequenceDiagram
  title  Selection
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
 
  rect rgb(191, 223, 255) 
  Borrower Platform (BAP)->>Lender Platform (BPP): select
  Lender Platform (BPP)-->>Borrower Platform (BAP):ACK
  end
  Lender Platform (BPP)->>Borrower Platform (BAP):on_select
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
```

## on_select_1

```mermaid
sequenceDiagram
  title  Selection
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
 
  
  Borrower Platform (BAP)->>Lender Platform (BPP): select
  Lender Platform (BPP)-->>Borrower Platform (BAP):ACK
  rect rgb(191, 223, 255) 
  Lender Platform (BPP)->>Borrower Platform (BAP):on_select
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  end
```

## on_status_1

```mermaid
sequenceDiagram
  title Initializing Order
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  participant Lender Form Service
  
  Borrower Platform (BAP)->>Lender Form Service: Get Form(KYC)
  Lender Form Service-->>Borrower Platform (BAP): Form Received
  Borrower Platform (BAP)->>Lender Form Service: Form Submission
  Lender Form Service-->>Borrower Platform (BAP): Submission ID
  rect rgb(191, 223, 255)
  Lender Platform (BPP)->>Borrower Platform (BAP):on_status
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  end
  Lender Platform (BPP)->>Borrower Platform (BAP):on_status
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  
```

## on_status_2

```mermaid
sequenceDiagram
  title Initializing Order
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  participant Lender Form Service
  
  Borrower Platform (BAP)->>Lender Form Service: Get Form(KYC)
  Lender Form Service-->>Borrower Platform (BAP): Form Received
  Borrower Platform (BAP)->>Lender Form Service: Form Submission
  Lender Form Service-->>Borrower Platform (BAP): Submission ID
 
  Lender Platform (BPP)->>Borrower Platform (BAP):on_status
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  rect rgb(191, 223, 255)
  Lender Platform (BPP)->>Borrower Platform (BAP):on_status
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  end
  
```

## on_status_3

```mermaid
sequenceDiagram
  title Initializing Order
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  rect rgb(191, 223, 255)
  Lender Platform (BPP)->>Borrower Platform (BAP):on_status
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  end
  Lender Platform (BPP)->>Borrower Platform (BAP):on_status
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  
```

## on_status_4

```mermaid
sequenceDiagram
  title Initializing Order
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
 
  Lender Platform (BPP)->>Borrower Platform (BAP):on_status
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  rect rgb(191, 223, 255)
  Lender Platform (BPP)->>Borrower Platform (BAP):on_status
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  end
  
```

## single_redirection

```mermaid
sequenceDiagram
  title Initializing Order
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  participant Lender Form Service
  rect rgb(191, 223, 255)
  Borrower Platform (BAP)->>Lender Form Service: Get Form(KYC)
  Lender Form Service-->>Borrower Platform (BAP): Form Received
  Borrower Platform (BAP)->>Lender Form Service: Form Submission
  Lender Form Service-->>Borrower Platform (BAP): Submission ID
  end
  Lender Platform (BPP)->>Borrower Platform (BAP):on_status
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  Lender Platform (BPP)->>Borrower Platform (BAP):on_status
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
 
```

## select_2

```mermaid
sequenceDiagram
  title  Selection
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
 
  rect rgb(191, 223, 255) 
  Borrower Platform (BAP)->>Lender Platform (BPP): select
  Lender Platform (BPP)-->>Borrower Platform (BAP):ACK
  end
  Lender Platform (BPP)->>Borrower Platform (BAP):on_select
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
```

## on_select_2

```mermaid
sequenceDiagram
  title  Selection
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
 
  
  Borrower Platform (BAP)->>Lender Platform (BPP): select
  Lender Platform (BPP)-->>Borrower Platform (BAP):ACK
  rect rgb(191, 223, 255) 
  Lender Platform (BPP)->>Borrower Platform (BAP):on_select
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  end
```

## on_confirm_1

```mermaid
sequenceDiagram
  title Order Confirmation
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  rect rgb(191, 223, 255)
  Lender Platform (BPP)->>Borrower Platform (BAP):on_confirm
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  end
```

## update_1

```mermaid
sequenceDiagram
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  Lender Platform (BPP)->>Borrower Platform (BAP):on_confirm
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  rect rgb(191, 223, 255)
  Borrower Platform (BAP)->>Lender Platform (BPP): update-Request (FORECLOSURE)
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
  end
  Lender Platform (BPP)->>Borrower Platform (BAP): on_update - Foreclosure quote
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  Lender Platform (BPP)->>Borrower Platform (BAP): on_update - Foreclosure quote
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
```

## on_update_1

```mermaid
sequenceDiagram
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  Lender Platform (BPP)->>Borrower Platform (BAP):on_confirm
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  
  Borrower Platform (BAP)->>Lender Platform (BPP): update-Request (FORECLOSURE)
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
  rect rgb(191, 223, 255)
  Lender Platform (BPP)->>Borrower Platform (BAP): on_update - Foreclosure quote
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  end
  Lender Platform (BPP)->>Borrower Platform (BAP): on_update - Foreclosure quote
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
```

## payment_url_form

```mermaid
sequenceDiagram
  title Payment Redirection
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  participant Payment Gateway
  Lender Platform (BPP)->>Borrower Platform (BAP): on_update (order.payments[0].url)
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  rect rgb(191, 223, 255)
  Borrower Platform (BAP)->>Payment Gateway: Redirect borrower using payment URL
  Payment Gateway-->>Borrower Platform (BAP): Payment completed
  end
  Lender Platform (BPP)->>Borrower Platform (BAP): on_update - Update success
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
```

## on_update_2

```mermaid
sequenceDiagram
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  Lender Platform (BPP)->>Borrower Platform (BAP):on_confirm
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  
  Borrower Platform (BAP)->>Lender Platform (BPP): update-Request (FORECLOSURE)
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
 
  Lender Platform (BPP)->>Borrower Platform (BAP): on_update - Foreclosure quote
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  rect rgb(191, 223, 255)
  Lender Platform (BPP)->>Borrower Platform (BAP): on_update - Foreclosure quote
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  end
```
