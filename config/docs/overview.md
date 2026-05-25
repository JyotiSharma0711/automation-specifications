# ONDC:FIS12 2.0.3 — Overview

## Summary
This domain enables credit products on ONDC, specifically gold loans and personal loans. It lets users discover and access loan offers from multiple lenders through a buyer app, compare terms, and complete their loan journey end-to-end with real-time updates from the lender.

## Sector & Purpose
**Sector**: Financial services, specifically consumer credit.

**Problem solved**: Users need a way to discover, compare, and apply for gold loans and personal loans without visiting multiple lenders independently. This domain brings lending products into the ONDC network so borrowers can transact with multiple lenders through a unified buyer app interface.

## Real-World Actors
According to the use case, the actors who transact are:
- **Borrowers**: Users who want a personal loan or gold loan
- **Lenders (Seller Apps)**: Banks and other financial institutions offering gold loans and personal loans

## Use Cases
- Discover and compare gold loan offers
- Apply for and receive a gold loan
- Discover and compare personal loan offers
- Apply for and receive a personal loan
- Track loan processing status in real-time
- Make EMI (monthly installment) payments and track loan balance
- Prepay part or all of a loan early
- Handle missed EMI payments
- Foreclose a loan completely before maturity

## Key Concepts
- **ONDC**: The open network protocol that connects buyer apps and lender apps
- **Credit Products**: Gold loans and personal loans offered by lenders to borrowers
- **Single Redirection**: Borrower selects a loan offer in the buyer app, then completes verification and signing on the lender's platform
- **Real-time Loan Tracking**: Lenders send status updates throughout the loan lifecycle so borrowers see progress without switching apps
- **EMI Management**: Monthly payment tracking and balance updates synchronized across the buyer app

## Example Scenario
A user opens a buyer app on the ONDC network looking to get a personal loan. The buyer app displays loan offers from several lender apps—different banks, each with their own interest rates and repayment terms. The user compares the options and selects a loan from their preferred bank. The buyer app redirects them to that bank's interface where they complete KYC verification, confirm their bank account, set up an auto-pay mandate, and sign the loan agreement. Once submitted, the bank processes the application in the background and sends real-time updates to the buyer app at each stage (submitted, verified, approved, disbursed) so the user can track progress without leaving the app. After the loan is disbursed, the user makes monthly EMI payments. Each time a payment posts, the bank sends an updated status to the buyer app showing the remaining balance and loan tenure, keeping the borrower's view synchronized with the lender's records.
