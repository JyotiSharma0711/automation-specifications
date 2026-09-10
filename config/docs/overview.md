# ONDC:FIS12 2.0.3 — Overview

## Summary

ONDC:FIS12 establishes a unified protocol for banks and loan providers to offer credit products—specifically Personal Loans and Gold Loans—through a common marketplace. A borrower using any buyer app can search, discover terms, and apply for loans across multiple lenders without switching platforms.

## Sector & Purpose

**Sector:** Financial services and lending.

**Problem Solved:** Traditionally, an individual seeking a personal or gold loan must visit each bank's website or branch separately, fill out distinct application forms, and wait for separate underwriting processes. This fragmentation makes comparison shopping difficult and slows credit access. ONDC:FIS12 creates a shared protocol so that credit products appear in a single marketplace—much like how ONDC unified e-commerce—allowing borrowers to discover and apply for multiple loan types in one buyer app, and enabling lenders to reach buyers without maintaining separate consumer channels.

## Real-World Actors

- **Buyers:** Individuals seeking personal loans or collateralized gold loans.
- **Loan Providers:** Banks, non-bank financial institutions (NBFCs), Primary (Urban) Co-operative Banks, and Regional Rural Banks.
- **Platform:** Buyer apps (powered by BAPs) that aggregate loan offers in real time.

## Use Cases

- **Unified Credit Discovery:** A borrower opens a buyer app and searches for "personal loan" or "gold loan" to see available offers and terms from multiple lenders.
- **Personal Loans (Unsecured):** Fast, digital-first unsecured loans evaluated based on borrower income, credit bureau data, and digital verification (KYC, e-Mandate, e-Sign).
- **Gold Loans (Secured):** Collateralized loans where physical gold ornaments/coins are pledged, combining digital offer discovery/selection with in-branch physical gold appraisal and offline underwriting.
- **Term Comparison:** Buyers compare loan amounts, interest rates, tenure, EMI, and eligibility criteria before applying.

## Key Concepts

- **Personal Loan:** An unsecured, collateral-free credit facility provided based on income and credit score.
- **Gold Loan:** A secured loan facility where physical gold is pledged as collateral and appraised at a lender's branch.
- **Account Aggregator (AA):** A consent-based data bridge enabling borrowers to share financial data with lenders for underwriting.
- **Single Redirection Journey:** A seamless flow where the borrower is redirected to the lender's hosted interface for KYC and verification, returning to the buyer app upon completion.
- **Offline Journey:** A flow where offline processing (such as physical gold valuation or field verification) occurs before final loan approval.

## Example Scenarios

**Scenario 1: Personal Loan Discovery & Application**

Ramesh opens his buyer app and searches for a personal loan of ₹2,00,000 for 24 months. The app queries participating banks and NBFCs. He compares interest rates, EMI amounts, and processing fees across multiple lenders, selects Bank A's offer, and completes instant KYC, e-Mandate, and e-Sign through the redirected journey.

**Scenario 2: Gold Loan with Branch Verification**

Sunita needs ₹1,50,000 and has gold jewellery to pledge as collateral. Through the buyer app, she searches for Gold Loans and selects her preferred local bank branch. After reviewing tentative bureau offers, she visits the chosen branch for physical gold appraisal. The lender completes the offline valuation and pushes real-time status updates back to her app until loan disbursal.
