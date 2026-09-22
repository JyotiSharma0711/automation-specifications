# Solar Purchase Finance

## Overview

Solar Purchase Finance is an asset-linked, secured variant of Purchase Finance on ONDC (referencing the `ONDC:FIS12` domain, version 2.3.0). Consumers purchasing rooftop solar systems often face high upfront equipment and installation costs (typically ₹1–3L post-subsidy). Without embedded, standardized point-of-sale financing, solar dealers and OEMs lose conversions at checkout. 

Today, solar financing is fragmented across bilateral lender–OEM partnerships. ONDC standardizes this by enabling an open, interoperable protocol where any buyer application (BAP) can discover, compare, and execute solar loan offers from any participating regulated lender (BPP) with zero bilateral integrations.

### Key Constructs

- **Asset-Linked Disbursal Gate**: Unlike unsecured purchase loans, loan disbursement for solar systems is strictly contingent upon installation completion. The lender pauses disbursement in a `PENDING_INSTALLATION` state until the buyer app verifies and attests to successful physical installation.
- **Merchant Subvention as a Pricing Construct**: Solar merchants/OEMs can fund interest costs as subvention (No-Cost or Low-Cost EMI) by declaring a maximum subvention percentage in the catalog, which lenders apply directly to reduce customer interest rates in binding offers.
- **Supported Solar Categories**: The protocol supports various rooftop solar configurations including **On-grid**, **Off-grid**, and **Hybrid** rooftop solar systems.
- **Standardized Onboarding**: Standardizes merchant identity (PAN/GST), disbursal destination bank accounts, and product specifications so lenders can underwrite both the merchant and the asset seamlessly.

## Participants

| Participant | Role in Solar Purchase Finance |
|-------------|--------------------------------|
| **Borrower (Buyer)** | Consumer purchasing a residential or commercial rooftop solar system on credit. |
| **Buyer App (BAP)** | Merchant-side, solar aggregator, or marketplace application surfacing loan offers at checkout and providing post-sanction installation attestation. |
| **Lender (BPP / Credit Seller)** | RBI-registered Regulated Entity (Scheduled Commercial Bank or NBFC) providing the solar purchase finance credit product and managing underwriting. |
| **Merchant / Solar Installer** | Solar OEM, authorized dealer, or EPC installer who receives the loan disbursal in their verified bank account upon installation completion. |
| **Account Aggregator (AA)** | RBI-licensed AA enabling electronic sharing of borrower bank statements for income verification. |
| **KYC & Verification Providers** | UIDAI / DigiLocker for Aadhaar eKYC, CKYC registries, and Credit Information Companies (CIEs) for credit assessment. |

## The User Journey

The Solar Purchase Finance lifecycle is divided into five core stages:

```
[ Discovery ] ──> [ Offer Generation ] ──> [ Loan Processing ] ──> [ Confirmation & Installation ] ──> [ Disbursal & Servicing ]
```

---

### 1. Discovery

The Buyer App (BAP) declares the use case as `SOLAR_PURCHASE_FINANCE` and broadcasts product and merchant parameters to lenders on the network.

#### Protocol Interaction
- **`/search`**: BAP broadcasts search intent containing merchant identifiers, verified disbursal bank account, product attributes, and maximum seller subvention percentage.
- **`/on_search`**: Lenders return their eligible solar purchase finance loan catalogs and underwriting criteria.

#### Discovery Parameters

| Group | Field | Type | Mandatory | Notes |
|-------|-------|------|-----------|-------|
| **Category** | Use-case code | Enum | Yes | `SOLAR_PURCHASE_FINANCE` |
| **Merchant Details** | PAN | String | Yes | Merchant entity PAN |
| | GST | String | Yes | GSTIN |
| **Merchant Bank Account** | Account Number | String | Yes | Disbursal destination account |
| | IFSC | String | Yes | Bank branch IFSC |
| | Account Holder Name | String | Yes | Must match penny-drop verification at lender |
| **Product Details** | Product Category | Enum | Yes | `On-grid`, `Off-grid`, or `Hybrid` rooftop system |
| | Brand | String | Yes | Solar OEM / Brand name (e.g., TATA Solar) |
| | Model | String | Yes | System model designation |
| | SKU ID | String | Yes | Unique catalog SKU identifier |
| | Price | Decimal (INR) | Yes | Total system cost to be financed (pre-downpayment) |
| | Max Seller Subvention (%) | Decimal | No | Ceiling of interest subsidy funded by the merchant |

---

### 2. Offer Generation & Selection

The borrower provides personal, professional, and loan configuration preferences (downpayment and tenure) alongside explicit bureau consent. Lenders evaluate creditworthiness and return personalized, binding loan offers.

#### Protocol Interaction
- **`/select`**: BAP submits borrower details, selected downpayment, requested tenure, bureau consent, and optional property details via lender-provided forms.
- **`/on_select`**: Lenders return binding Key Fact Statement (KFS) offers including sanctioned-in-principle loan amount, net interest rate (incorporating subvention), EMI schedule, processing fees, and offer TTL.

#### Offer Configuration Fields

| Group | Field | Type | Mandatory | Description / Notes |
|-------|-------|------|-----------|---------------------|
| **Personal** | Name | String | Yes | As per PAN; baseline for KYC matching |
| | Personal Email | Email | Yes | Primary email contact |
| | Official Email | Email | Conditional | Mandatory if Employment Type = `SALARIED` |
| | Date of Birth | Date | Yes | Standard `YYYY-MM-DD` |
| | Gender | Enum | Yes | `MALE`, `FEMALE`, `OTHER` |
| | PAN | String | Yes | Borrower PAN number |
| | Contact Number | String | Yes | 10-digit mobile number |
| | Address (Pincode) | String | Yes | Installation / residential pincode |
| **Employment** | Employment Type | Enum | Yes | `SALARIED` or `SELF_EMPLOYED` |
| | Monthly Income | Decimal (INR) | Yes | Net monthly income |
| | Employer Name | String | No | Company / Business name |
| | Years of Experience | String | No | Professional vintage |
| **Loan Structure** | Downpayment | Decimal (INR) | Yes | Initial payment borne by borrower |
| | Tenure | Integer | Yes | Loan duration in months |
| **Consent** | Bureau Consent | Boolean | Yes | Explicit checkbox consent for credit bureau pull |

#### Optional Offer-Widening Parameters
Alongside mandatory fields, the protocol allows optional parameters such as **Property Details** (Property Ownership Status, Property Type, Installation Site Address).
- Skipping optional fields never blocks the journey; the borrower receives offers from all lenders whose mandatory criteria are satisfied.
- When provided, lenders with specific asset/property underwriting requirements return offers in the same `/on_select` cycle without requiring a new search.

---

### 3. Loan Processing & Agreement Signing

Once an offer is selected, the lender guides the borrower through sequential fulfillment steps.

#### Protocol Interaction
- **`/init`**: BAP submits underwriting documents, completed KYC details, e-mandate setup, and repayment account details.
- **`/on_init`**: Lender presents forms/redirection URLs for e-mandate registration, repayment bank account verification (penny drop), loan agreement eSign (LBA eSign), and downpayment collection.

#### Sequential Fulfillment Steps
1. **Document Verification**: Upload or reference of mandatory underwriting documents:
   - **Electricity Bill Number (e-bill no.)**: Establishes installation site ownership/residency and historical consumption baseline.
   - **Bank Statement / Financial Data**: Sourced via Account Aggregator (AA) or document upload for income verification.
2. **KYC Verification**: Completed via Aadhaar OTP, Central KYC (CKYC), or Video KYC (VKYC) per lender policy.
3. **eMandate Setup**: Borrower registers auto-debit repayment mandate (NACH / UPI Autopay).
4. **Repayment Bank Account Verification**: Penny-drop / name-match confirmation of borrower's account.
5. **Loan Agreement Execution (LBA eSign)**: Borrower digitally signs the loan agreement via Aadhaar eSign.
6. **Downpayment Collection**: Downpayment is paid by the borrower via the lender's payment gateway (a hard gate before order confirmation).

---

### 4. Order Confirmation & Installation-Gated Disbursal

In Solar Purchase Finance, loan sanction is decoupled from loan disbursal to ensure funds are released only when the solar system is physically delivered and installed.

```
INITIATED ──> SANCTIONED (LOAN_SANCTIONED)
                 │
                 ▼
          PENDING_INSTALLATION
                 │ (BAP Installation Attestation)
                 ▼
          INSTALLATION_CONFIRMED
                 │
                 ▼
          DISBURSED (Funds sent to Merchant Account)
```

#### Protocol Interaction
- **`/confirm`**: BAP submits confirmation with downpayment receipt and executed loan agreement.
- **`/on_confirm`**: Lender transitions order to `LOAN_SANCTIONED`, confirms loan ID, and places disbursal in `PENDING_INSTALLATION` state.
- **`/update`**: Once physical solar installation is completed at the site, the BAP sends an update carrying the installation-confirmed fulfillment state (including timestamp and attestation reference).
- **`/on_update` / `on_status`**: Lender acknowledges attestation, transitions state to `INSTALLATION_CONFIRMED`, triggers loan disbursal directly to the merchant's bank account, and emits unsolicited `on_status` with the disbursal UTR (Unique Transaction Reference).

---

### 5. Post-Disbursal Servicing

Borrowers can manage active loans directly through the BAP using the standard FIS12 servicing capabilities:

- **EMI Schedule & Payment Status**: Real-time retrieval of upcoming instalments and past payment history via `/status`.
- **Pre-Part Payment & Foreclosure**: Borrower can request partial prepayment or full loan foreclosure via `/update`; lender returns exact payment links and charges in `/on_update`.
- **Missed EMI Handling**: Automated penalty and overdue disclosures with direct payment links.

## Additional Scenarios

### 1. Cancellation Before Installation & Disbursal
If the order is cancelled prior to installation:
- The BAP notifies the lender via `/update` (order cancellation).
- The lender voids the sanctioned loan agreement and initiates a refund of the borrower's downpayment.

### 2. Product Returns or Installation Failures
If installation cannot be completed due to structural or technical infeasibility:
- The BAP notifies the lender before installation attestation is submitted.
- The loan is voided without disbursing funds to the merchant, and any collected downpayment is refunded net of applicable inspection charges per policy.

### 3. Loan Pre-Payment & Late Payments
- **Late Payments**: Lenders communicate overdue amounts and generate on-demand payment links.
- **Pre-Payment / Foreclosure**: Lenders return absolute fee breakdowns (principal, accrued interest, foreclosure charges) before redirecting to the payment gateway.

## Loan States

| # | Loan State | Description |
|---|------------|-------------|
| 1 | **Sanctioned** | Loan amount approved and sanctioned for the solar rooftop system. |
| 2 | **Sanctioned & Downpayment Collected** | Sanctioned, and downpayment confirmed via payment gateway. |
| 3 | **Pending Installation** | Disbursal held pending BAP site installation verification. |
| 4 | **Installation Confirmed** | BAP installation attestation received and verified by lender. |
| 5 | **Disbursed to Merchant** | Loan funds disbursed directly to the solar installer/merchant account. |
| 6 | **Void post Sanction** | Sanctioned loan voided prior to installation/disbursal. |
| 7 | **Cancelled** | Disbursed loan closed/cancelled following formal return/cancellation process. |
| 8 | **Pre-Paid / Closed** | Loan fully repaid prior to tenure completion or closed upon maturity. |

## Issue and Grievance Management

IGM handling in Solar Purchase Finance follows standard FIS12 protocols, allowing buyer apps and lenders to utilize unified grievance mechanisms for transaction disputes, installation delays, and servicing requests.