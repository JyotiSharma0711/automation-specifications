# business term loan without aa with igm 1.0.0 — Sequence Diagrams

Internal data file consumed by the Developer Guide's "Sequence Diagram" tab (API Walkthrough).
Not meant to be shown as its own docs page — the frontend filters this slug out of the Use Case
Brief / Additional Resources / Changelog tab lists and instead looks up the section matching the
selected API call's `action_id` (the `##` heading below) to render that step's diagram.

One `## <action_id>` heading per step of `business_term_loan_without_aa_with_igm_1.0.0.yaml`, in that flow's own step order, each
followed by its Mermaid `sequenceDiagram`.

The issue/on_issue/issue_status/on_issue_status steps (IGM) have no counterpart in ONDC-FIS-Specifications -- their diagrams are drafted from the standard ONDC IGM protocol shape, the same generic diagrams already used for the other FIS12 product lines' IGM flows.

## search_1

```mermaid
sequenceDiagram
  title  Business Loan Discovery
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
  title  Business Loan Discovery
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
 
  Borrower Platform (BAP)->>Lender Platform (BPP): search
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
  rect rgb(191, 223, 255)
  Lender Platform (BPP)->>Borrower Platform (BAP):on_status
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  end
  Lender Platform (BPP)->>Borrower Platform (BAP):on_status
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  
  Lender Platform (BPP)->>Borrower Platform (BAP):on_status
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK

  
```

## on_status_2

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
  Lender Platform (BPP)->>Borrower Platform (BAP):on_status
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK

  
```

## on_status_3

```mermaid
sequenceDiagram
  title Initializing Order
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  
  Lender Platform (BPP)->>Borrower Platform (BAP):on_status
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  
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
  # Lender Platform (BPP)->>Borrower Platform (BAP):on_status
  # Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  # Lender Platform (BPP)->>Borrower Platform (BAP):on_status
  # Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
```

## issue_open_100

```mermaid
sequenceDiagram
  title Issue & Grievance Management
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  rect rgb(191, 223, 255)
  Borrower Platform (BAP)->>Lender Platform (BPP): issue - Raise a complaint
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
  end
  Lender Platform (BPP)->>Borrower Platform (BAP): on_issue - Complaint acknowledged
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  Borrower Platform (BAP)->>Lender Platform (BPP): issue_status - Request complaint status
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
  Lender Platform (BPP)->>Borrower Platform (BAP): on_issue_status - Complaint status (PROCESSING)
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  Lender Platform (BPP)->>Borrower Platform (BAP): on_issue_status - Complaint resolved
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  Borrower Platform (BAP)->>Lender Platform (BPP): issue - Close the complaint
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
```

## on_issue_processing_100

```mermaid
sequenceDiagram
  title Issue & Grievance Management
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  Borrower Platform (BAP)->>Lender Platform (BPP): issue - Raise a complaint
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
  rect rgb(191, 223, 255)
  Lender Platform (BPP)->>Borrower Platform (BAP): on_issue - Complaint acknowledged
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  end
  Borrower Platform (BAP)->>Lender Platform (BPP): issue_status - Request complaint status
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
  Lender Platform (BPP)->>Borrower Platform (BAP): on_issue_status - Complaint status (PROCESSING)
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  Lender Platform (BPP)->>Borrower Platform (BAP): on_issue_status - Complaint resolved
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  Borrower Platform (BAP)->>Lender Platform (BPP): issue - Close the complaint
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
```

## issue_status_processing_100

```mermaid
sequenceDiagram
  title Issue & Grievance Management
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  Borrower Platform (BAP)->>Lender Platform (BPP): issue - Raise a complaint
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
  Lender Platform (BPP)->>Borrower Platform (BAP): on_issue - Complaint acknowledged
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  rect rgb(191, 223, 255)
  Borrower Platform (BAP)->>Lender Platform (BPP): issue_status - Request complaint status
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
  end
  Lender Platform (BPP)->>Borrower Platform (BAP): on_issue_status - Complaint status (PROCESSING)
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  Lender Platform (BPP)->>Borrower Platform (BAP): on_issue_status - Complaint resolved
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  Borrower Platform (BAP)->>Lender Platform (BPP): issue - Close the complaint
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
```

## on_issue_status_processing_100

```mermaid
sequenceDiagram
  title Issue & Grievance Management
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  Borrower Platform (BAP)->>Lender Platform (BPP): issue - Raise a complaint
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
  Lender Platform (BPP)->>Borrower Platform (BAP): on_issue - Complaint acknowledged
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  Borrower Platform (BAP)->>Lender Platform (BPP): issue_status - Request complaint status
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
  rect rgb(191, 223, 255)
  Lender Platform (BPP)->>Borrower Platform (BAP): on_issue_status - Complaint status (PROCESSING)
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  end
  Lender Platform (BPP)->>Borrower Platform (BAP): on_issue_status - Complaint resolved
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  Borrower Platform (BAP)->>Lender Platform (BPP): issue - Close the complaint
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
```

## on_issue_resolved_100

```mermaid
sequenceDiagram
  title Issue & Grievance Management
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  Borrower Platform (BAP)->>Lender Platform (BPP): issue - Raise a complaint
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
  Lender Platform (BPP)->>Borrower Platform (BAP): on_issue - Complaint acknowledged
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  Borrower Platform (BAP)->>Lender Platform (BPP): issue_status - Request complaint status
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
  Lender Platform (BPP)->>Borrower Platform (BAP): on_issue_status - Complaint status (PROCESSING)
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  rect rgb(191, 223, 255)
  Lender Platform (BPP)->>Borrower Platform (BAP): on_issue_status - Complaint resolved
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  end
  Borrower Platform (BAP)->>Lender Platform (BPP): issue - Close the complaint
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
```

## issue_close_100

```mermaid
sequenceDiagram
  title Issue & Grievance Management
  participant Borrower Platform (BAP)
  participant Lender Platform (BPP)
  Borrower Platform (BAP)->>Lender Platform (BPP): issue - Raise a complaint
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
  Lender Platform (BPP)->>Borrower Platform (BAP): on_issue - Complaint acknowledged
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  Borrower Platform (BAP)->>Lender Platform (BPP): issue_status - Request complaint status
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
  Lender Platform (BPP)->>Borrower Platform (BAP): on_issue_status - Complaint status (PROCESSING)
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  Lender Platform (BPP)->>Borrower Platform (BAP): on_issue_status - Complaint resolved
  Borrower Platform (BAP)-->>Lender Platform (BPP): ACK
  rect rgb(191, 223, 255)
  Borrower Platform (BAP)->>Lender Platform (BPP): issue - Close the complaint
  Lender Platform (BPP)-->>Borrower Platform (BAP): ACK
  end
```
