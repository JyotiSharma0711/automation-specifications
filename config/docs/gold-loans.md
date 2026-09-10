# Gold Loans on ONDC — Developer Guide

## Gold Loan (ONDC FIS12 - Credit)

## On this page

- [Overview](#overview)
- [Participants](#participants)
- [The User Journey](#the-user-journey)
  - [1. Product Discovery](#1-product-discovery)
  - [2. Application Form and Bureau Offer Selection](#2-application-form-and-bureau-offer-selection)
  - [3. Branch Selection and Final Offer](#3-branch-selection-and-final-offer)
  - [4. Offline Verification and Underwriting](#4-offline-verification-and-underwriting)
  - [5. Loan Confirmation](#5-loan-confirmation)
- [Additional Scenarios](#additional-scenarios)
  - [1. Missed EMI Payment](#1-missed-emi-payment)
  - [2. Part-Payment](#2-part-payment)
  - [3. Foreclosure](#3-foreclosure)
- [Issue and Grievance Management](#issue-and-grievance-management)

---

## Overview

A Gold Loan lets a borrower pledge physical gold ornaments or coins as collateral for a loan. The digital front door is the same as a Personal Loan — a borrower searches, compares offers, and applies online through a Loan Service Provider (LSP). The difference is what happens next: because the collateral is physical gold, it has to be appraised in person, so everything after offer selection — verification, valuation, and underwriting — happens offline at the lender's branch, with the lender pushing periodic status updates back to the LSP until final approval or rejection.

Each lender independently manages its own Gold Loan products, appraisal process, pricing, and servicing. ONDC enables these lenders and lending apps to connect through a common, open protocol instead of building separate integrations with each other.

---

## Participants

| Participant | What This Means |
|---|---|
| **Lender** | An RBI-regulated lending institution that offers Gold Loan products on the network. Responsible for the branch network where gold is appraised, the appraisal and underwriting process itself, sanction, disbursal, and servicing. |
| **Lending App (Loan Service Provider)** | A buyer application that offers Gold Loan products to its users by connecting with participating lenders through the ONDC network. The LSP handles applicant intake, offer comparison, branch selection, and relays offline verification status to the borrower until a decision is reached. |
| **Borrower** | An individual pledging physical gold as collateral for a loan. Unlike a fully digital product, the borrower needs to physically visit the chosen branch at some point in the journey for gold appraisal. |

---

## The User Journey

The Gold Loan journey enables a borrower to discover offers, choose a lender and branch, and receive a loan once the lender has physically appraised the pledged gold. The journey consists of the following stages:

### 1. Product Discovery

The LSP searches the network for available Gold Loan services.

**Network interaction:**

- **`/search`**: The LSP sends a discovery request tagged with the `GOLD_LOAN` category — and, distinctively for this product, a `OFFLINE_CONTRACT` tag set to `true`, signaling upfront that this journey resolves offline rather than end-to-end digitally.
- **`/on_search`**: Each lender returns a static catalogue of its loan types, including Gold Loans.

### 2. Application Form and Bureau Offer Selection

The borrower fills in an application form (formId: `FO1`) with:

- User Type — Individual or Non-Individual
- PAN, Full Name, Constitution (for non-individual entities)
- Gender, Employment type (Salaried or Self Employment), Date of Birth
- Annual Income, Contact number, Email
- Address, Pincode, City, State
- Jewellery (gms) and Purity (24K, 22K, 21K, 18K, 14K, or 9K) — the pledged gold itself, unique to this product
- End Use — Marriage, Family Functions, Medical Treatment and Emergencies, Travel/Education Expenses, Business Expansion, Agriculture and Farm-Related Needs, Purchase of Equipment, or Others
- Bureau Consent (checkbox)

The form's markup still has a commented-out Account Aggregator ID field. It's present in the DOM but disabled, not deleted — consistent with this being the "without AA" journey rather than AA never having been considered for Gold Loan. Don't build against it unless it's explicitly re-enabled.

**Network interaction:**

- **`/select`**: The LSP submits the completed form's submission ID, choosing the bureau-based loan item.
- **`/on_select`**: The lender responds with the list of branch locations where this Gold Loan service is available — a step unique to Gold Loan, since the borrower will need to pick a branch for the physical part of the journey.

### 3. Branch Selection and Final Offer

The borrower picks their preferred location from the list.

**Network interaction:**

- **`/select`**: The LSP sends the borrower's chosen location.
- **`/on_select`**: The lender returns the available loan offer(s) for that specific location, along with the next application form (KYC).

### 4. Offline Verification and Underwriting

This is where the Gold Loan journey diverges from a Personal Loan. There's no `/init`/`/on_init` redirection cycle here — instead, once the KYC form is submitted, the LSP tracks progress through repeated, lender-initiated status pushes while the borrower's gold is physically appraised and underwriting is completed at the branch.

**Network interaction:**

- **`/status`**: The LSP requests the current state of the application.
- **`/on_status`**: The lender responds — and continues to push further unsolicited `/on_status` updates as appraisal and underwriting progress. During this period, the status is reported as `OFFLINE_PENDING`; once verification and underwriting conclude, the lender sends a final `/on_status` marked `COMPLETED`.

Because this stage can span multiple branch visits and manual steps, expect several `OFFLINE_PENDING` pushes in sequence rather than a single wait-then-resolve call. The LSP's borrower-facing messaging should reflect "in appraisal/verification" as its own state — this is a normal, expected part of a Gold Loan application, not a stalled or failed one.

### 5. Loan Confirmation

Once the lender's `/on_status` reports `COMPLETED`, the LSP confirms the booking.

**Network interaction:**

- **`/confirm`**: The LSP confirms the Gold Loan request.
- **`/on_confirm`**: The lender confirms the order and shares final loan details.

---

## Additional Scenarios

Once the loan is confirmed and disbursed, Gold Loan servicing follows the same single-order pattern as a Personal Loan — there's no base-order/child-order split here, since a Gold Loan is a single term facility rather than a revolving line.

### 1. Missed EMI Payment

**Network interaction:**

- **`/update`**: The borrower requests missed-EMI payment details, referencing the order ID.
- **`/on_update`**: The lender returns the payment details, and — once paid — confirms success.

### 2. Part-Payment

**Network interaction:**

- **`/update`**: The borrower requests to make a partial prepayment, referencing the order ID.
- **`/on_update`**: The lender returns the payment details, and — once paid — confirms success.

### 3. Foreclosure

**Network interaction:**

- **`/update`**: The borrower requests full foreclosure of the loan, referencing the order ID.
- **`/on_update`**: The lender returns the foreclosure payment details, and — once paid — confirms success, at which point the pledged gold is released back to the borrower.

---

## Issue and Grievance Management

IGM handling is standardized across FIS12, so an LSP or lender that has already implemented IGM for another FIS12 lending product should be able to reuse that implementation for Gold Loan rather than building a separate grievance pipeline.
