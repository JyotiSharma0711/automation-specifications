# Purchase Finance



- [Overview](#overview)
  - [Supported Product Categories](#supported-product-categories)
- [Participants](#participants)
- [The User Journey](#the-user-journey)
  - [1. Loan Offer Discovery](#1-loan-offer-discovery)
  - [2. Offer Selection, KYC & Seller Account Validation](#2-offer-selection-kyc--seller-account-validation)
  - [3. Loan Agreement Signing & Disbursal Setup](#3-loan-agreement-signing--disbursal-setup)
  - [4. Disbursal](#4-disbursal)
- [Additional Scenarios](#additional-scenarios)
  - [1. Cancellation Before Disbursal](#1-cancellation-before-disbursal)
  - [2. Product Returns After Disbursal](#2-product-returns-after-disbursal)
  - [3. Partial Cancellation in a Multi-Cart Order](#3-partial-cancellation-in-a-multi-cart-order)
  - [4. Loan Pre-Payment and Late Payment](#4-loan-pre-payment-and-late-payment)
- [Loan States](#loan-states)
- [Issue and Grievance Management](#issue-and-grievance-management)

## Overview

Purchase Finance is an independent protocol that works for commerce occurring both on the ONDC network and off the network (such as external e-commerce platforms or physical retail checkouts). It is ONDC's version of what the market knows as checkout finance or Buy Now, Pay Later (BNPL) - the same mechanic behind buying an iPhone "on EMI" at a retailer or e-commerce checkout instead of paying the full price upfront. A customer discovers a loan offer within a buyer app, mostly at checkout (though some buyer apps surface it earlier, during product browsing), and converts a purchase into EMIs on the spot rather than applying for credit separately.

One market-standard variant worth calling out by name: No-Cost EMI, where the brand or seller funds the interest cost as a discount, so the customer's total repayment equals the sticker price rather than sticker-price-plus-interest. This is exactly what the protocol calls seller subvention - the retail seller declaring how much of the interest it's willing to absorb, expressed as a percentage of the product's selling price. Whether an offer looks like a standard interest-bearing EMI or a No-Cost EMI to the customer depends entirely on how much subvention the seller is willing to fund, the underlying loan mechanics are identical either way.

Each lender independently manages its own purchase finance products, underwriting, and servicing. ONDC enables these lenders and credit buyer apps to connect through a common, open protocol instead of building separate integrations with each other.

### Supported Product Categories

The protocol supports purchase financing across multiple retail categories:

- **Currently Supported**:
  - **Electronics** (e.g., smartphones, laptops, appliances)
  - **Residential Solar Rooftop** (Resi Solar Rooftop)
- **Upcoming**:
  - **Insurance Premium Finance**

This guide explains the Purchase Finance use case and end-to-end journey from a business and product perspective, before covering the corresponding technical specifications and API flows.

## Participants

| Participant | What This Means |
|-------------|-----------------|
| Lender (Credit Seller) | An RBI-registered Regulated Entity - Scheduled Commercial Bank, NBFC, Primary (Urban) Co-operative Bank, or Regional Rural Bank - offering purchase finance credit on the network. |
| Credit Buyer App | The application through which the borrower discovers and applies for the loan offer. Can be any application adhering to prevailing RBI guidelines. |
| Retail Buyer App | The application or aggregator facilitating the purchase of the retail/commerce product itself, operating either on the ONDC network or off-network. In several scenarios (such as e-commerce marketplaces conducting commerce outside ONDC), the Retail Buyer App and the Credit Buyer App can be the same entity. |
| Retail Seller App | The aggregator or platform representing sellers of the retail/commerce product, operating either on the ONDC network or off-network. |
| Account Aggregator (AA) | RBI-licensed AAs let borrowers share bank statements electronically with lenders. Invocation is optional and left to the Credit Buyer App's discretion based on product type and price. |
| KYC & Credit Bureau Providers | UIDAI and DigiLocker for eKYC, RBI-regulated Credit Information Companies for the borrower's credit history. |

## The User Journey

The Purchase Finance journey enables a borrower to discover a loan offer at the point of buying a product, get approved, and have the lender disburse funds directly to the seller - rather than to the borrower. The journey consists of the following stages:

### 1. Loan Offer Discovery

The Retail Buyer App gauges the retail seller's intent to participate in purchase finance for a specific product (if the customer wants it), and whether the seller will fund interest as subvention - and if so, the maximum subvention as a percentage of the product's selling price. It shares product details, the seller's (or seller aggregator's) PAN, bank account number, and maximum seller subvention with the Credit Buyer App.

The Credit Buyer App then captures:

- Product information - category, brand, SKU number, price net of discount
- Borrower details - phone number, PAN number, address
- Loan tenure preference (in multiples of 3 months) and the downpayment amount the borrower is willing to pay
- Seller's subvention % - the lever behind a No-Cost EMI–style offer: the more interest the seller subsidizes here, the closer the customer's total repayment gets to the plain sticker price

...and broadcasts this as one packet to multiple lenders on the network. The Credit Buyer App also prompts the borrower for AA-based financial-data consent - this is optional, invoked at the Credit Buyer App's discretion depending on product type and price.

Network interaction:

| API | Description |
|-----|-------------|
| `/search` | The Credit Buyer App queries the network for available Purchase Loan services. |
| `/on_search` | Each lender returns its static catalogue of loan types, including Purchase Loans. |

This is followed by two further `/search`/`/on_search` rounds, each carrying a lender-supplied form submission:

- A merchant & product details form - seller/seller-aggregator PAN and GST, bank account holder name/number/IFSC, product brand/category/model/price/SKU/return period, and whether financing applies to this product.
- A personal details form - the borrower's PAN, name, DOB, gender, employment type, income, contact and email, address, city, state, tenure, downpayment, end use, UDYAM number (where applicable), and bureau consent.

Each lender processes this within a defined duration and returns an offer including: Maximum Loan Amount, Offer Type (an array of tenures and corresponding downpayment requirements), standard KFS terms, and any subvention discount. The Credit Buyer App displays all offers received, showing all key parameters per RBI's digital lending guidelines (per KFS) and any subvention discount.

### 2. Offer Selection, KYC & Seller Account Validation

Upon offer selection, the lender triggers one of two workflows: Straight-Through Processing (if the customer already has a relationship with the lender and KYC isn't required), or KYC Initiation (eKYC, video KYC, cKYC, etc., chosen by the lender depending on loan ticket size).

The Credit Buyer App shares the seller's (or seller aggregator's) disbursal bank account with the lender, which validates it and confirms success before disbursal proceeds. Key parameters validated:

- Mandatory: Seller's/Seller Aggregator's Name, Account Number, and PAN/GST Number
- Optional: the seller's fraud history (as maintained by the lender), and ONDC Rating & Badges (e.g., an authorized brand dealer)

Network interaction:

| API | Description |
|-----|-------------|
| `/select` | The Credit Buyer App notifies the lender of the offer chosen. |
| `/on_select` | The lender responds, and - across further `/select`/`/on_select` rounds - may present a form to adjust the loan amount/tenure, and then the KYC form where required. |

### 3. Loan Agreement Signing & Disbursal Setup

Once KYC and seller account validation succeed, the lender sends a success acknowledgment. The borrower then sets up a repayment mandate on their repayment bank account, the lender shares the loan agreement for digital signature, and the Credit Buyer App prompts the borrower to pay the downpayment via the lender's payment gateway.

Network interaction:

| API | Description |
|-----|-------------|
| `/init` | The Credit Buyer App submits the KYC form and, in a further round, the e-mandate/account-details form. |
| `/on_init` | The lender provides the e-mandate form - the downpayment is collected as part of the same mandate redirection flow - and subsequently the e-sign form for the loan agreement. |
| `/confirm` | The Credit Buyer App submits the signed agreement. |
| `/on_confirm` | The lender confirms the Purchase Loan order. |

A confirmation of the downpayment being completed by the customer is necessarily required before disbursement can proceed - this is a hard gate, not a formality.

### 4. Disbursal

The loan amount is disbursed to the seller's (or seller aggregator's) account only once all of the following are satisfied, as applicable:

- Successful confirmation of product delivery by the retail seller (or logistics service provider)
- Successful sharing of the Serial Number/IMEI with the lender (for electronics purchases)
- Confirmation of the product return period having lapsed - where the Credit Buyer App has shared the product's return window with the lender

Network interaction:

| API | Description |
|-----|-------------|
| `/update` | The Credit Buyer App notifies the lender as each disbursal condition (delivery, serial/IMEI, return-window) is satisfied. |
| `/on_update` | The lender updates the order's fulfillment state accordingly and, once disbursed, sends a further unsolicited `/on_update` sharing the UTR (Unique Transaction Reference) of the disbursal. The Credit Buyer App relays this UTR to the Retail Seller App. |

## Additional Scenarios

### 1. Cancellation Before Disbursal

If the customer cancels the commerce order before receiving the product: the Credit Buyer App receives a cancel order-status update from the Retail Buyer App, and passes this on to the lender.

Network interaction:

| API | Description |
|-----|-------------|
| `/update` | The Credit Buyer App notifies the lender of the commerce-side cancellation. |
| `/on_update` | The lender voids the loan disbursal (the signed loan agreement is cancelled) and refunds the downpayment collected from the customer. |

### 2. Product Returns After Disbursal

Three sub-scenarios apply once the borrower has received the product:

- Exact replacement - the Credit Buyer App and lender aren't involved at all.
- Different replacement product - not a supported scenario for purchase-finance-enabled products, seller aggregators must convey this to retail buyer applications as part of their retail agreements.
- Refund - handled differently depending on whether disbursal has already happened:
  - Before the lender has disbursed the loan amount: the loan is voided by the lender, shared with the Credit Buyer App, and the downpayment is refunded by the buyer app/lender.
  - After the lender has disbursed the loan amount:

Network interaction:

| API | Description |
|-----|-------------|
| `/cancel` - soft cancel | The Credit Buyer App requests cancellation. |
| `/on_cancel` - SOFT_CANCEL | The lender acknowledges, sharing cancellation terms including any applicable cancellation/foreclosure fee. |
| `/cancel` - confirm cancel | The Credit Buyer App confirms the cancellation. |
| `/on_cancel` - CANCELLED | The lender confirms the loan is cancelled. |
| `/on_update` (unsolicited) | The lender shares the updated payment status - the downpayment refund (net of any deducted charges) appears as its own payment entry. |

Money movement for this scenario: Any foreclosure charges/penalties (per the loan agreement) are collected from the borrower either via a separate payment link or by deduction from the refunded downpayment. The lender separately collects back the disbursed loan amount from the seller aggregator/seller. Any interest/principal already paid is settled with the borrower per the lender's policy. The seller aggregator's collection of cancellation/refund charges from the buyer application (per their own retail agreement).

### 3. Partial Cancellation in a Multi-Cart Order

Purchase finance for a multi-cart scenario is supported only when the same seller sold every product in the purchase-financing cart. The lender receives a product-wise cancellation flag from the Credit Buyer App and can proceed with partial loan cancellation - voiding just that portion of the loan. Any downpayment collected for the cancelled product is refunded after deducting applicable foreclosure/cancellation charges.

### 4. Loan Pre-Payment and Late Payment

The Credit Buyer App lets borrowers view active and inactive loans and, for active loans, take three actions: late payment, part-prepayment, or full repayment (foreclosure).

Network interaction:

| API | Description |
|-----|-------------|
| `/update` | The Credit Buyer App notifies the lender of the selected action. |
| `/on_update` | The lender generates a payment link and returns the amount, charges, and payment link - in absolute values, not percentages - for the borrower to review. The lender returns an error if the operation isn't supported or the request is invalid. |

The Credit Buyer App displays the breakup to the borrower before redirecting them to the lender's payment gateway URL.

## Loan States

| # | Loan State | Description |
|---|-----------|-------------|
| 1 | Sanctioned | The loan amount requested has been sanctioned for the purchase. |
| 2 | Sanctioned & Downpayment Collected | Sanctioned, and the downpayment has been successfully collected by the lender/buyer app. |
| 3 | Disbursed to Seller | The full amount (product price net of seller discounts, if any) has been disbursed to the seller/seller aggregator. Can only be invoked after sanction. |
| 4 | Void post Sanction | The sanctioned loan stands void. Can only be invoked before disbursal to the seller. |
| 5 | Cancelled | The disbursed loan stands cancelled. Can only be invoked after disbursal to the seller. |
| 6 | Pre-Paid | The disbursed loan has been prepaid before the defined tenure. Can only be invoked after disbursal to the seller. |

## Issue and Grievance Management

IGM handling is standardized across FIS12, so a Credit Buyer App or lender that has already implemented IGM for another FIS12 lending product should be able to reuse that implementation for Purchase Finance rather than building a separate grievance pipeline.
