# Personal Loans & Gold Loans — ONDC FIS12 - Credit

## On this page

- [Personal Loans (ONDC FIS12 - Credit - 2.0.3)](#personal-loans--ondc-fis12---credit---203)
  - [Overview & Use Case Brief](#overview--use-case-brief)
  - [Participants](#participants)
  - [The User Journey](#the-user-journey)
  - [Additional Scenarios](#additional-scenarios)
  - [Issue and Grievance Management](#issue-and-grievance-management)
  - [Detailed Technical Protocol Flows](#detailed-technical-protocol-flows)
- [Gold Loans (ONDC FIS12 - Credit)](#gold-loans--ondc-fis12---credit)
  - [Overview](#gold-loan-overview)
  - [Participants](#gold-loan-participants)
  - [The User Journey](#gold-loan-user-journey)
  - [Additional Scenarios](#gold-loan-additional-scenarios)
  - [Issue and Grievance Management](#gold-loan-issue-and-grievance-management)

---

# Personal Loans — ONDC FIS12 - Credit - 2.0.3

## Overview & Use Case Brief

Personal loans are unsecured, collateral-free loans offered by banks and NBFCs based on factors such as the borrower’s income, credit profile, and eligibility. Each lender independently manages its loan products, underwriting, pricing, terms, application process, and servicing.

ONDC enables these lenders and lending apps to connect through a common, open protocol instead of building separate integrations with each other. A lending app integrates with the ONDC network as a Loan Service Provider (LSP) and can discover and offer loan products from participating lenders. Lenders integrate once with the network to make their loan products available to participating lending apps.

The lender remains responsible for the loan product, including eligibility, underwriting, approval, pricing, terms, disbursal, and servicing. ONDC standardizes the network interactions for discovering, comparing, applying for, and servicing personal loans across participating network participants.

This guide explains the personal loan use case and end-to-end journey from a business and product perspective, before covering the corresponding technical specifications and API flows.

---

## Participants

| Participant | What This Means |
|---|---|
| **Lender** | An RBI-regulated lending institution that offers personal loan products on the network. This includes Scheduled Commercial Banks, NBFCs, Primary (Urban) Co-operative Banks, and Regional Rural Banks. The lender is responsible for the loan product, including eligibility, underwriting, approval, pricing, disbursal, and servicing. |
| **Lending App (Loan Service Provider)** | A buyer application that offers personal loan products to its users by connecting with participating lenders through the ONDC network. This can include lending, payments, e-commerce, or personal finance applications. The LSP facilitates loan discovery and application while the lender remains responsible for credit assessment and lending decisions, in accordance with applicable RBI guidelines. |

---

## The User Journey

The personal loan journey enables a borrower to discover loan offers, select a lender, complete the lender's onboarding and verification process, and receive the loan. The journey consists of the following stages:

### 1. Loan Application and Discovery

The borrower provides their basic information through the Lending App (LSP), including:

- PAN
- Mobile number
- Name
- Pincode
- Date of birth
- Employment type — salaried or self-employed
- Income
- Employer name
- UDYAM number, where applicable for self-employed borrowers
- Bureau consent

The LSP verifies the borrower's mobile number through OTP and obtains the required consent to share the information with participating lenders and allow lenders to access the borrower's credit bureau information.

The LSP then sends the loan search request to participating lenders through the network.

**Network interaction:**

- **`/search`**: The LSP sends the borrower's loan requirements, including the requested loan amount, tenure, and personal loan category.
- **`/on_search`**: Participating lenders respond with their available loan products and relevant parameters such as loan amount range, tenure, interest rate, processing fees, and applicable product attributes.

### 2. Loan Offers

Based on the information available to them, lenders return loan offers that may include:

- Bureau-based offers
- Tentative offers subject to additional information or verification

The LSP presents the available offers to the borrower for comparison.

The borrower can compare parameters such as loan amount, interest rate, tenure, EMI, and applicable fees.

### 3. Offer Selection

The borrower selects a loan offer through the LSP.

**Network interaction:**

- **`/select`**: The LSP sends the selected loan product.
- **`/on_select`**: The lender responds with the applicable loan quote, including APR, processing fees, EMI details, and other applicable charges or terms and the link to continue the loan processing journey.

### 4. Lender Onboarding and Verification

After the borrower selects an offer, the borrower proceeds to the lender's onboarding journey, which is rendered within the LSP experience (app-in-app experience).

The lender is responsible for determining and executing the required onboarding and verification steps. These may include:

- KYC and identity verification
- Bank account verification
- Repayment mandate setup
- Loan agreement execution

The specific verification method may vary by lender.

#### KYC
The lender may use methods such as Aadhaar OTP, offline eKYC, Video KYC, liveness checks, DigiLocker, field verification, or other permitted verification methods.

#### Bank Account Verification
The lender verifies the borrower's bank account using methods such as penny-drop verification or account-holder name matching.

#### Repayment Setup
The lender sets up the mechanism for collecting future EMIs. This may include eMandate, eNACH, UPI AutoPay, or standing instructions.

#### Loan Agreement
The borrower executes the loan agreement using the method supported by the lender, such as clickwrap or Aadhaar-based e-sign.

The lender communicates the status of these activities to the LSP through asynchronous `/on_status` updates.

### 5. Final Underwriting and Loan Offer

The lender completes its credit assessment using the information available to it and any additional information collected during the onboarding journey.

Where required, the borrower may be asked to provide additional documents, such as bank statements in PDF format. The lender uses this information along with bureau and other relevant data to complete its underwriting.

The lender then generates the final loan offer, including the applicable loan amount, pricing, tenure, EMI, fees, and other terms.

The lender communicates the status of the final offer through `/on_status`.

> **Account Aggregator:** Account Aggregator is not part of this network flow. This can be carried out by the lender in its journey to enhance the offered amount or ROI.

### 6. Application Status and Processing

The lender sends asynchronous (unsolicited) `/on_status` updates to the LSP throughout the loan journey. These updates keep the LSP informed of the borrower's application status without requiring the LSP to manage the lender's internal processing.

The status updates can cover the following stages:

| Stage | Purpose |
|---|---|
| `KYC` | Tracks the progress and outcome of identity verification. |
| `LOAN_OFFER` | Indicates generation and acceptance of the final loan offer. |
| `BANK_ACCOUNT_VERIFICATION` | Indicates the status of bank account verification. |
| `REPAYMENT` | Indicates the status of mandate or repayment setup. |
| `LOAN_AGREEMENT` | Indicates the status of agreement execution and provides the signed agreement once completed. |

### 7. Offline Processing

A lender may require manual verification or processing that cannot be completed through the digital journey. This may include field verification, branch checks, telephone verification, or manual underwriting.

In such cases, the lender sends an `/on_status` update indicating that the application is `IN_PROGRESS` and that processing is continuing offline.

Once the offline activity is completed, the lender sends another `/on_status` update with the outcome:

- **`SUCCESSFUL`** — The application can proceed with the remaining digital steps.
- **`FAILED`** — The application is rejected, along with the applicable rejection information.

The LSP uses these updates to communicate the application status to the borrower.

### 8. Loan Confirmation and Disbursement

Once all required onboarding activities are successfully completed, the LSP sends `/confirm` to the lender.

The lender validates the completed journey and confirms the loan booking through `/on_confirm`.

The lender then shares the relevant loan details, which may include:

- Loan Account ID
- Disbursal or remittance details
- Repayment schedule

The lender disburses the loan amount to the borrower's bank account.

After disbursement, the loan moves into the repayment stage. The lender continues to share relevant loan status updates with the LSP, including updates associated with subsequent EMI payments.

---

## Additional Scenarios

The personal loan journey continues after loan booking through loan servicing, repayment, and grievance management. The network supports the following additional scenarios.

### 1. Loan Servicing and Repayment

After disbursement, the borrower can view the status of their active and closed loans through the Lending App (LSP). Regular EMI collection continues through the repayment mandate set up with the lender.

The lender sends relevant loan and repayment status updates to the LSP through `/on_status`, allowing the LSP to keep the borrower's loan information up to date.

The borrower can initiate the following servicing actions for an active loan, subject to the lender's applicable policies:

- Pay a missed or overdue EMI
- Make a part-prepayment
- Foreclose the loan by making full repayment

The lender determines whether the requested action is applicable to the loan and calculates the amount payable, including any applicable charges.

### 2. Missed EMI Payment

A borrower can make a manual payment when an EMI has not been successfully collected through the configured repayment mandate.

**Network interaction:**

- **`/update`**: The LSP sends a repayment servicing request to the lender, identifying the action as a `LATE_PAYMENT` request.
- **`/on_update` / `/on_status`**: The lender validates the request and returns the outstanding amount, applicable charges, and payment link or payment instructions.
- **`/on_status`**: After successful payment, the lender updates the loan account and sends the payment status and updated outstanding information to the LSP.

The LSP displays the applicable dues and payment status to the borrower.

### 3. Part-Prepayment

A borrower can make a partial repayment towards the outstanding loan principal, subject to the lender's product terms and applicable regulations.

**Network interaction:**

- **`/update`**: The LSP sends a `PART-PREPAYMENT` request with the amount the borrower intends to repay.
- **`/on_update` / `/on_status`**: The lender validates the request and returns the applicable amount, charges, and payment link or payment instructions.
- **`/on_status`**: After successful payment, the lender updates the outstanding principal and provides the revised repayment information, including the updated EMI or repayment schedule where applicable.

Applicable prepayment charges and conditions are determined by the lender and must be communicated to the borrower in accordance with applicable regulations and product terms.

### 4. Loan Foreclosure

A borrower can request full repayment of an active loan before the scheduled end of its tenure, subject to the lender's applicable terms and regulations.

**Network interaction:**

- **`/update`**: The LSP sends a `FORECLOSURE` request for the selected loan.
- **`/on_update` / `/on_status`**: The lender calculates the total foreclosure amount and returns the applicable outstanding principal, accrued interest, charges, and payment link or payment instructions.
- **`/on_status`**: After successful payment, the lender updates the loan account as fully repaid and sends the updated loan status to the LSP.

The lender is responsible for calculating and disclosing applicable foreclosure or prepayment charges. For certain floating-rate personal loans to individual borrowers, RBI regulations restrict the levy of foreclosure/prepayment penalties.

### 5. Loan Status After Repayment

After a successful part-prepayment, missed EMI payment, or foreclosure, the lender updates the loan account and communicates the latest status to the LSP through `/on_status`.

For a fully repaid loan, the lender marks the loan as closed and provides the relevant closure or repayment information supported by the network.

---

## Issue and Grievance Management

A borrower can raise a grievance through the LSP for issues related to their loan or the network transaction. The LSP routes the grievance to the relevant lending partner through the network's grievance mechanism.

The lender is responsible for investigating and resolving the grievance. The lender communicates the grievance status and resolution to the LSP, which makes the relevant information available to the borrower.

---

## Detailed Technical Protocol Flows

### Flow 1: Personal Loan – Single Redirection Journey

#### 1. Short Description
The Single Redirection Flow allows the borrower to discover and select loan offers within the Buyer App, then is redirected to the lender’s interface for completing KYC, bank verification, mandate setup, and agreement signing. The lender shares loan processing progress in real time through asynchronous `on_status` updates while the borrower completes the journey. 
Post every EMI payment, `on_status` is sent to the buyer app to be in sync.

#### 2. API Breakdown & Technical Actions
- **`/search` (BAP $\rightarrow$ Gateway)**: Triggered when a borrower searches for a loan. The BAP broadcasts the loan requirements, specifying the domain category (`intent.category = "PERSONAL_LOAN"`), the requested loan amount, and the target repayment tenure across the network gateway.
- **`/on_search` (BPP $\rightarrow$ BAP)**: Lenders evaluate the preliminary filtering data and respond asynchronously with their structural product catalogs (`catalog.items[]`). This payload includes interest rate metrics, loan amount ranges, tenure parameters, and processing fee allocations. It also features descriptor tags (`loan_type`, `co_lending`, `aa_required`) so the BAP can render the options accurately.
- **`/select` (BAP $\rightarrow$ BPP)**: Initiated when the borrower selects a specific loan product. The BAP opens a direct point-to-point connection to that lender, passing the specific product identifier (`order.items[id]`) along with the desired loan sum and tenure.
- **`/on_select` (BPP $\rightarrow$ BAP)**: The lender returns a personalized, itemized financial quote containing the finalized Annual Percentage Rate (APR), processing fees, monthly EMI breakdown, and prepayment penalties. If additional pre-qualification data is required (such as a PAN or stated income), the lender can embed an `xinput` form layout here to capture data before the next phase.
- **`/on_status` (BPP $\rightarrow$ BAP)**: An asynchronous background webhook pipeline used by the lender to push real-time status updates to the BAP as the borrower completes milestones within the redirected interface:
  - **KYC Stage**: Tracks identity verification states (`INITIATED` $\rightarrow$ `IN_PROGRESS` $\rightarrow$ `SUCCESSFUL` / `FAILED`) and notes the verification mode used (e.g., `AADHAR`, `VKYC`, `LIVENESS`).
  - **LOAN_OFFER Stage**: Signals when the final underwritten terms are generated (`FINALIZED`) and when the user clicks to accept the contract (`SELECTED`).
  - **REPAYMENT Stage**: Tracks automatic monthly debit setup via electronic mandates (`E-MANDATE`) or bank standing instructions (`SI`).
  - **BANK_ACCOUNT_VERIFICATION Stage**: Confirms account validation using automated penny-drop deposits or database name-matching checks (`PENNYLESS`).
  - **LOAN_AGREEMENT Stage**: Monitors contract execution (`CLICKWRAP` or `AADHAR_ESIGN`), returning a direct download link to the signed PDF contract once marked `SUCCESSFUL`.
- **`/confirm` (BAP $\rightarrow$ BPP)**: Executed after the borrower completes the external journey and returns to the parent application. The BAP verifies that all onboarding webhooks reached a status of `SUCCESSFUL` and sends a final confirmation payload, using the `form_submission_id` from the return parameters to validate session integrity.
- **`/on_confirm` (BPP $\rightarrow$ BAP)**: Confirms that the loan has been officially booked in the lender's core banking system. The lender sets the network record state to `ACTIVE` and provides the official Loan Account ID, remittance values, and the permanent amortization schedule.

---

### Flow 2: Personal Loan – Offline Journey

#### 1. Short Description
The Offline Journey Flow is used when a loan application requires manual verification or operational checks outside the lender’s digital journey. Instead of completing onboarding fully online, the borrower is informed that the application will continue through offline processing such as field verification, branch checks, or manual underwriting. The lender continues updating the application progress asynchronously through `on_status` callbacks until the loan is approved, rejected, or completed.

#### 2. API Mechanics & System Purposes
- **`/on_status` [Offline Hold State] (BPP $\rightarrow$ BAP)**: When an application hits a rule that requires manual review, the lender triggers an `/on_status` call with the operational state set to `IN_PROGRESS`. The payload includes descriptive custom tags that signal a pause in automated processing. This allows the BAP to update its internal interface, showing the user that their application is in review while the lender's hosted window updates to its static hold view.
- **`/on_status` [Resumption Trigger] (BPP $\rightarrow$ BAP)**: Once offline verifications or field visits are complete, the lender's backend system fires a new `/on_status` payload. This pushes either a `SUCCESSFUL` status (with finalized credit details) or a `FAILED` status (with explicit rejection codes) to restore the digital session. This notification alerts the BAP that it can now prompt the borrower to return and finish the application.
- **`/confirm` & `/on_confirm` (BAP $\leftrightarrow$ BPP)**: Standard execution blocks run post-resumption to formally finalize the application and trigger fund disbursement.

---

### Flow 3: Personal Loan – Dedupe Check

#### 1. Short Description
The Dedupe Check Flow is used to identify existing or duplicate loan applications before the lender proceeds with underwriting or offer generation. Lenders evaluate borrower identifiers and existing records to detect active journeys, pre-approved offers, or duplicate applications across onboarding stages. This helps reduce redundant processing, avoid unnecessary bureau pulls, and improve overall onboarding efficiency across the network.

#### 2. API Mechanics & System Purposes

| API Call | System & Operational Target | Role in Dedupe Identification |
|---|---|---|
| **`/search`** | Network Broadcast | Transmits basic search criteria across the gateway. Lenders run a preliminary check on the incoming mobile or PAN string to see if the user has an active application file or an existing relationship in core systems. |
| **`/on_search`** | Catalog Delivery | If an existing customer (ETB) relationship or recent application conflict is identified, the lender can adjust its catalog response, returning specialized pre-approved offers or withholding options. |
| **`/select` / `/on_select`** | Direct Validation | The borrower interacts directly with the chosen lender. If the system identifies a duplicate application or policy conflict, it bypasses quote generation and returns a direct error packet or application rejection code (e.g., **Error Code `50002` for Policy Rejection**). |

---

### Flow 4: Personal Loan – Loan Foreclosure (Full Repayment)

#### 1. Architectural Introduction & Ecosystem Challenges Solved
The Loan Foreclosure Flow simplifies full account termination by integrating the process directly into the network architecture. Post-disbursal, a borrower can choose to foreclose their entire loan before the planned tenure ends.
When initiated, this flow automates the query process across the lender's core systems to calculate the exact, up-to-the-minute closure values required for full settlement. The lender calculates these charges based on regulatory and internal guidelines, factoring in the loan's current lifecycle status and any applicable `COOL_OFF_PERIOD` rules.
The lender then delivers an instant digital settlement path directly to the BAP interface.

```
[Borrower Requests Foreclosure] ───► [/update Request Triggers Payoff Calculation] ───► [Lender Returns Exact Breakout & Pay Link] ───► [Settlement & Account Closure]
```

#### 2. API Mechanics & System Purposes
- **`/update` (BAP $\rightarrow$ BPP)**: Initiates a post-disbursal loan modification request. The payload sets the target object to `REPAYMENT` and appends servicing tags that label the transaction specifically as a `FORECLOSURE` request.
- **`/on_update` / `/on_status` (BPP $\rightarrow$ BAP)**: The lender's system processes the request and calculates the total payoff amount. It returns a detailed financial breakout containing the remaining principal balance, interest accrued up to the current date, and any applicable foreclosure penalties based on `COOL_OFF_PERIOD` guidelines. This response includes a secure payment gateway link, allowing the BAP to display the full cost breakdown before routing the borrower to complete the payment.
- **Second `/on_status` Push [Post-Payment Execution] (BPP $\rightarrow$ BAP)**: Triggered after the payment clears through the designated gateway. The lender updates its system logs, marks the account balance as zero, and pushes an updated status callback with `fulfillment.state = SUCCESSFUL` and `order.state = COMPLETED` to close out the loan record.

---

### Flow 5: Personal Loan – Pre-Part Payment

#### 1. Short Description
The Pre-Part Payment Flow allows borrowers to make partial repayments toward their outstanding loan principal outside their regular EMI cycle. The lender validates the request, calculates applicable charges or revised repayment impact, and returns a payment link or repayment instructions through the protocol. Once the payment is completed successfully, the lender recalculates the remaining loan schedule and updates the borrower’s future repayment structure.

#### 2. API Mechanics & System Purposes
- **`/update` (BAP $\rightarrow$ BPP)**: Sends an ad-hoc servicing instruction to the chosen lender. The payload carries specific tags that identify the action as a `PART-PREPAYMENT` and declares the exact amount the borrower intends to pay down.
- **`/on_update` / `/on_status` (BPP $\rightarrow$ BAP)**: The lender's system evaluates the request against its credit guidelines to check if the partial payment amount meets its minimum thresholds. If approved, it generates a payment tracking reference and returns an absolute financial breakout (Amount and Charges) along with a secure payment gateway link. The BAP displays this clear breakdown to the borrower before safely routing them to the payment gateway.
- **Subsequent `/on_status` Update (BPP $\rightarrow$ BAP)**: Once the transaction is successfully processed, the lender's core banking systems adjust the loan parameters. The lender fires a confirmation webhook containing the updated remaining principal balance and the modified future EMI restructure schedule, keeping the BAP's interface fully synchronized.

---

### Flow 6: Personal Loan – Missed EMI Payment (Late Payment)

#### 1. Short Description
The Missed EMI Payment Flow allows borrowers to manually repay overdue EMIs when automatic collections fail due to insufficient balance or mandate issues. The lender calculates the pending dues, penalties, and applicable charges, and returns a payment link or repayment method through the protocol. Once the borrower completes the payment, the lender reconciles the amount and updates the repayment status across the network.

```
[Auto-Debit Fails / Overdue State] ───► [Borrower Requests Late-Payment Link] ───► [Lender Returns Core EMI + Accumulated Penalties] ───► [Instant Self-Cure Clear]
```

#### 2. API Mechanics & System Purposes
- **`/update` (BAP $\rightarrow$ BPP)**: The BAP initiates a retrieval request for a past-due loan account. It passes a servicing payload with transaction tags set specifically to `LATE_PAYMENT` to request the outstanding overdue balance.
- **`/on_update` / `/on_status` (BPP $\rightarrow$ BAP)**: The lender's billing systems calculate the total outstanding balance. The response returns an explicit cost breakdown containing the original missed EMI amount, any late payment penalties, and account bounce fees. This includes an active payment gateway link, allowing the BAP to show the full breakdown before routing the user to complete the payment.
- **`/on_status` [Remittance Resolution] (BPP $\rightarrow$ BAP)**: Fired immediately after the payment clears through the designated gateway. The lender updates its internal ledgers, marks the past-due balance as settled, resets the account status to current, and returns the updated payment confirmation reference to the parent app.

---
---

# Gold Loans — ONDC FIS12 - Credit

## <a id="gold-loan-overview"></a>Overview

A Gold Loan lets a borrower pledge physical gold ornaments or coins as collateral for a loan. The digital front door is the same as a Personal Loan — a borrower searches, compares offers, and applies online through a Loan Service Provider (LSP). The difference is what happens next: because the collateral is physical gold, it has to be appraised in person, so everything after offer selection — verification, valuation, and underwriting — happens offline at the lender's branch, with the lender pushing periodic status updates back to the LSP until final approval or rejection.

Each lender independently manages its own Gold Loan products, appraisal process, pricing, and servicing. ONDC enables these lenders and lending apps to connect through a common, open protocol instead of building separate integrations with each other.

---

## <a id="gold-loan-participants"></a>Participants

| Participant | What This Means |
|---|---|
| **Lender** | An RBI-regulated lending institution that offers Gold Loan products on the network. Responsible for the branch network where gold is appraised, the appraisal and underwriting process itself, sanction, disbursal, and servicing. |
| **Lending App (Loan Service Provider)** | A buyer application that offers Gold Loan products to its users by connecting with participating lenders through the ONDC network. The LSP handles applicant intake, offer comparison, branch selection, and relays offline verification status to the borrower until a decision is reached. |
| **Borrower** | An individual pledging physical gold as collateral for a loan. Unlike a fully digital product, the borrower needs to physically visit the chosen branch at some point in the journey for gold appraisal. |

---

## <a id="gold-loan-user-journey"></a>The User Journey

The Gold Loan journey enables a borrower to discover offers, choose a lender and branch, and receive a loan once the lender has physically appraised the pledged gold. The journey consists of the following stages:

### 1. Product Discovery

The LSP searches the network for available Gold Loan services.

**Network interaction:**

- **`/search`**: The LSP sends a discovery request tagged with the `GOLD_LOAN` category — and, distinctively for this product, an `OFFLINE_CONTRACT` tag set to `true`, signaling upfront that this journey resolves offline rather than end-to-end digitally.
- **`/on_search`**: Each lender returns a static catalogue of its loan types, including Gold Loans.

### 2. Application Form and Bureau Offer Selection

The borrower fills in an application form (`formId: FO1`) with:
- **User Type**: Individual or Non-Individual
- **Identity & Demographics**: PAN, Full Name, Constitution (for non-individual entities), Gender, Employment type (Salaried or Self Employment), Date of Birth
- **Financials & Contact**: Annual Income, Contact number, Email, Address, Pincode, City, State
- **Jewellery & Collateral**: Jewellery (gms) and Purity (`24K`, `22K`, `21K`, `18K`, `14K`, or `9K`) — the pledged gold itself, unique to this product
- **End Use**: Marriage, Family Functions, Medical Treatment and Emergencies, Travel/Education Expenses, Business Expansion, Agriculture and Farm-Related Needs, Purchase of Equipment, or Others
- **Bureau Consent**: Consent checkbox

> **Note on Account Aggregator**: The form's markup still has a commented-out Account Aggregator ID field. It's present in the DOM but disabled, not deleted — consistent with this being the "without AA" journey rather than AA never having been considered for Gold Loan. Don't build against it unless it's explicitly re-enabled.

**Network interaction:**

- **`/select`**: The LSP submits the completed form's submission ID, choosing the bureau-based loan item.
- **`/on_select`**: The lender responds with the list of branch locations where this Gold Loan service is available — a step unique to Gold Loan, since the borrower will need to pick a branch for the physical part of the journey.

### 3. Branch Selection and Final Offer

The borrower picks their preferred location from the list.

**Network interaction:**

- **`/select`**: The LSP sends the borrower's chosen location.
- **`/on_select`**: The lender returns the available loan offer(s) for that specific location, along with the next application form (KYC).

### 4. Offline Verification and Underwriting

This is where the Gold Loan journey diverges from a Personal Loan. There's no `/init` / `/on_init` redirection cycle here — instead, once the KYC form is submitted, the LSP tracks progress through repeated, lender-initiated status pushes while the borrower's gold is physically appraised and underwriting is completed at the branch.

**Network interaction:**

- **`/status`**: The LSP requests the current state of the application.
- **`/on_status`**: The lender responds — and continues to push further unsolicited `/on_status` updates as appraisal and underwriting progress. During this period, the status is reported as `OFFLINE_PENDING`; once verification and underwriting conclude, the lender sends a final `/on_status` marked `COMPLETED`.

> **Status Tracking**: Because this stage can span multiple branch visits and manual steps, expect several `OFFLINE_PENDING` pushes in sequence rather than a single wait-then-resolve call. The LSP's borrower-facing messaging should reflect "in appraisal/verification" as its own state — this is a normal, expected part of a Gold Loan application, not a stalled or failed one.

### 5. Loan Confirmation

Once the lender's `/on_status` reports `COMPLETED`, the LSP confirms the booking.

**Network interaction:**

- **`/confirm`**: The LSP confirms the Gold Loan request.
- **`/on_confirm`**: The lender confirms the order and shares final loan details.

---

## <a id="gold-loan-additional-scenarios"></a>Additional Scenarios

Once the loan is confirmed and disbursed, Gold Loan servicing follows the same single-order pattern as a Personal Loan — there's no base-order/child-order split here, since a Gold Loan is a single term facility rather than a revolving line.

### <a id="1-missed-emi-payment-gold"></a>1. Missed EMI Payment

**Network interaction:**

- **`/update`**: The borrower requests missed-EMI payment details, referencing the order ID.
- **`/on_update`**: The lender returns the payment details, and — once paid — confirms success.

### <a id="2-part-payment-gold"></a>2. Part-Payment

**Network interaction:**

- **`/update`**: The borrower requests to make a partial prepayment, referencing the order ID.
- **`/on_update`**: The lender returns the payment details, and — once paid — confirms success.

### <a id="3-foreclosure-gold"></a>3. Foreclosure

**Network interaction:**

- **`/update`**: The borrower requests full foreclosure of the loan, referencing the order ID.
- **`/on_update`**: The lender returns the foreclosure payment details, and — once paid — confirms success, at which point the pledged gold is released back to the borrower.

---

## <a id="gold-loan-issue-and-grievance-management"></a>Issue and Grievance Management

IGM handling is standardized across FIS12, so an LSP or lender that has already implemented IGM for another FIS12 lending product should be able to reuse that implementation for Gold Loan rather than building a separate grievance pipeline.
