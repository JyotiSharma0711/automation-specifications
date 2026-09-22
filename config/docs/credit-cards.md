# Credit Card

- [Overview](#overview)
- [Participants](#participants)
- [The User Journey](#the-user-journey)
  - [1. Product Discovery](#1-product-discovery)
  - [2. Personal Information Application Form](#2-personal-information-application-form)
  - [3. Card Selection and KYC Form](#3-card-selection-and-kyc-form)
  - [4. KYC Verification and Status Polling](#4-kyc-verification-and-status-polling)
  - [5. Application Initiation](#5-application-initiation)
  - [6. Confirmation and Dispatch](#6-confirmation-and-dispatch)
  - [7. Final Status Tracking](#7-final-status-tracking)
- [Issue and Grievance Management](#issue-and-grievance-management)

---

## Overview

A Credit Card journey lets a borrower discover, apply for, and receive a credit card entirely through the ONDC network — from browsing a lender's card catalogue to tracking the physical card's dispatch. Unlike Gold Loan, there's no branch visit required: card selection, KYC verification, and confirmation all happen through hosted forms and network calls, with the lender only pushing offline-style status updates while the applicant's KYC is being verified.

Each lender independently manages its own credit card products, benefits, fees, and KYC/underwriting process. ONDC enables these lenders and lending apps to connect through a common, open protocol instead of building separate integrations with each other.

---

## Participants

| Participant | What This Means |
|---|---|
| **Lender** | An RBI-regulated bank or NBFC that offers credit card products on the network (e.g. HDFC Bank in the reference catalogue). Responsible for the card catalogue, benefit terms, KYC verification, sanction, and physical card dispatch. |
| **Lending App (BAP)** | A buyer application that offers credit card products to its users by connecting with participating lenders through the ONDC network. Handles applicant intake, hosts the application/KYC forms, and relays status updates to the borrower until the card is dispatched. |
| **Borrower / Applicant** | An individual applying for a credit card. Completes two hosted forms during the journey — a personal-information application form and a KYC verification step — but never needs to visit a branch in person. |

---

## The User Journey

The Credit Card journey enables a borrower to discover card offers, apply with personal and KYC details, and track the application through to card dispatch. The journey consists of the following stages:

### 1. Product Discovery

The BAP searches the network for available credit card offerings.

**Network interaction:**

- **`/search`**: The BAP sends a discovery request scoped to the `CREDIT_CARD` category, along with its `BAP_TERMS` tag (terms-of-engagement URL and an `OFFLINE_CONTRACT` flag).
- **`/on_search`**: The lender returns its catalogue — provider details, categories (`CARD` → `CREDIT_CARD` → e.g. `PREMIUM_CARDS`/`TRAVEL_CARDS`/`REWARDS_CARDS`/`LIFESTYLE_CARDS`), and one or more card items. Each item carries a `GENERAL_INFO` tag list describing its welcome benefit, joining/annual fee, rewards rate, APR (where applicable), travel/lifestyle/everyday benefits, and terms-and-conditions link, plus the provider's own `CONTACT_INFO`/`LSP_INFO` tags (grievance officer, customer support, LSP details). Each item also carries an `xinput` block pointing the BAP at the personal-information application form it must collect next.

### 2. Personal Information Application Form

The applicant fills out the hosted application form referenced by the selected item's `xinput.form.url` from `on_search`.

**Form fields:** Name as per PAN, personal/official email, date of birth, gender, PAN, contact number, employment type, income, company name, address (line 1/2, city, state, pin code), a derived-data file upload, and bureau consent.

### 3. Card Selection and KYC Form

The BAP submits the completed application form's submission ID against the chosen card, and the lender responds with the next form the applicant needs — this time for KYC.

**Network interaction:**

- **`/select`**: The BAP echoes the chosen provider and item, attaching the personal-information form's `xinput.form_response` (status + submission ID).
- **`/on_select`**: The lender confirms the selected card and attaches a new `xinput` block — a "Know your Customer" navigation head plus a fresh form reference — pointing the BAP at the KYC verification step.

### 4. KYC Verification and Status Polling

Because KYC verification can take time, the lender models progress the same way Gold Loan does its offline appraisal: the applicant completes the KYC step, and the lender pushes status updates until verification concludes.

**Network interaction:**

- The applicant completes the KYC verification form.
- **`/on_status`** (unsolicited): The lender pushes the item's `xinput.form_response.status` as `OFFLINE_PENDING` while KYC is still being verified.
- **`/status`** → **`/on_status`**: The BAP can also poll directly; once verification concludes, the lender responds with `xinput.form_response.status` set to `COMPLETED`.

### 5. Application Initiation

Once KYC is confirmed complete, the BAP initiates the credit card request.

**Network interaction:**

- **`/init`**: The BAP submits the order carrying the completed KYC form's submission ID (`xinput.form_response.status: SUCCESS`) along with its `BAP_TERMS` tag.
- **`/on_init`**: The lender accepts the request, echoing the card's benefit details and introducing fulfillment tracking — a customer contact record with an initial `INITIATED` state.

### 6. Confirmation and Dispatch

The BAP confirms the application, and the lender finalizes the order and ships the physical card.

**Network interaction:**

- **`/confirm`**: The BAP confirms the request, now carrying both `BAP_TERMS` and `BPP_TERMS` tags.
- **`/on_confirm`**: The lender mints the order ID, sets order status to `ACTIVE`, and moves the fulfillment to `DISPATCHED`, attaching shipping details (AWB number, shipping partner, delivery address).

### 7. Final Status Tracking

The BAP can check the latest application/dispatch status at any point after confirmation.

**Network interaction:**

- **`/status`**: The BAP requests the current state of the order, referencing the order ID.
- **`/on_status`**: The lender responds with the full confirmed order — provider, item, fulfillment (including shipping details), and terms tags.

---

## Issue and Grievance Management

IGM handling is standardized across FIS12, so a lending app or lender that has already implemented IGM for another FIS12 lending product should be able to reuse that implementation for Credit Card rather than building a separate grievance pipeline.
