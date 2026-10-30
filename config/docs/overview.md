# Loan Against Mutual Funds (LAMF)

---

## Overview

A Loan Against Mutual Funds lets an investor borrow against their mutual fund holdings without selling them. Because the units stay in the borrower's name (merely lien-marked, not transferred), the borrower keeps earning dividends/growth and avoids triggering capital gains tax or exit loads that a redemption would cause. It sits between "sell your investments" and "take an unsecured loan" — cheaper and faster than a personal loan or credit card for the borrower, and a secured, historically low-NPA asset for the lender.

Each lender independently manages its loan products, underwriting, eligible-unit logic, pricing, and servicing. ONDC enables these lenders and lending apps to connect through a common, open protocol instead of building separate integrations with each other. A lending app integrates with the ONDC network as a Loan Service Provider (LSP) and can discover and offer LAMF products from participating lenders. Lenders integrate once with the network to make their LAMF products available to participating lending apps.

LAMF runs on ONDC Tunnel, the network's common routing layer for credit. Participants send every LAMF call to the Tunnel endpoint, and Tunnel decides who receives it based on what each side has declared on the ONDC portal.

This guide explains the LAMF use case and end-to-end journey from a business and product perspective, before covering the corresponding technical specifications and API flows. Network interactions in this guide reference the `ONDC:FIS12:SL` domain, version 2.3.0 (`draft-FIS12-2.3.0-SL`).

---

## ONDC Tunnel for LAMF

Tunnel is a routing and validation layer, similar to the switch that routes UPI payments. It carries and checks LAMF messages; it does not underwrite, price, hold collateral, or make lending decisions. Those decisions, and all statutory reporting, stay with the lender as the regulated entity.

Three Tunnel capabilities are live for LAMF:

| Capability | What it does for LAMF | What it replaces |
|---|---|---|
| **Whitelist / blacklist declarations on the ONDC portal** | Lenders declare which LSPs they accept LAMF traffic from; LSPs declare their lender preferences. Tunnel routes each request only to counterparties those declarations allow. | Private lender lists and per-pair whitelists in each participant's own systems, updated every time a counterparty is added or dropped. |
| **Schema validation** | Every request and response is checked against the network specification before it is routed. A non-conforming message is rejected back to its sender and never reaches the counterparty. | Errors discovered late, inside the counterparty's system or mid-journey. |
| **Real-time network observability dashboard** | Tunnel logs every message it routes and shows LAMF transaction health across the network in real time. | Participants sharing operational logs separately with Network Observability; visibility limited to each participant's own connections. |

A call that fails either check stops at Tunnel. Lender responses, including unsolicited margin calls, pass the same schema check on the way back to the LSP.

Schema validation confirms that a message is well-formed and spec-conformant. It does not check business rules such as offer staleness, eligible units, or KYC outcomes — those stay with the LSP and the lender, as the journey stages below note.

Running LAMF on Tunnel is a configuration exercise, not a rebuild. Each participant needs to:

1. Point all LAMF API calls at the Tunnel endpoint.
2. Register participation details and declare whitelist/blacklist preferences on the ONDC portal.
3. Conform to the baselined FIS12 version for LAMF — payloads that don't conform are rejected at Tunnel.
4. Stop routing on private lender lists and let Tunnel route.
5. Complete end-to-end LAMF testing on the pre-production environment before production rollout.

---

## Participants

| Participant | What This Means |
|---|---|
| **Lender** | An RBI-regulated lending institution (bank or NBFC) that offers LAMF products on the network. The lender is responsible for AMC/scheme tie-ups, underwriting eligible units, pricing, lien marking, disbursal or limit setup, and servicing — including margin monitoring and liquidation. On Tunnel, the lender declares on the ONDC portal which LSPs it accepts LAMF traffic from. |
| **Lending App (Loan Service Provider)** | A buyer application that offers LAMF products to its users by connecting with participating lenders through the ONDC network. The LSP handles applicant intake, portfolio discovery, offer comparison, pledge adjustment, and redirects the borrower into the lender's environment for every step the lender executes directly. On Tunnel, the LSP declares its lender preferences on the portal instead of maintaining a private lender list. |
| **Borrower / Investor** | An individual or entity holding mutual fund investments who needs liquidity. This isn't limited to natural persons — a Sole Proprietorship firm is a valid user type, so KYC and eligibility logic should not assume a single-individual applicant in every case. |
| **Account Aggregator (AA)** | An NBFC-AA that, with borrower consent, shares aggregated financial data. AA adoption in the LAMF journey specifically has been limited in practice, with MF Central (or an equivalent aggregator) doing most of the portfolio-discovery work instead — treat AA as a supported-but-secondary path, not the primary data rail. |
| **RTA / Depository (NSDL/CDSL)** | The Registrar and Transfer Agent (e.g., CAMS, KFintech) is the system of record for MF unit holdings and executes lien marking for folio-held units. Where units are held in demat form via a broker, lien marking runs through the depository instead. A single borrower's holdings can span both, so implementations need to branch per holding, not just per borrower. |
| **ONDC Tunnel** | The network's routing and validation layer for credit, operated by ONDC. It routes LAMF messages according to portal declarations, validates them against the specification, and feeds the network observability dashboard. It is not a party to the loan. |

---

## The User Journey

The LAMF journey enables a borrower to discover offers against their MF portfolio, select a lender, complete the lender's onboarding and pledge process, and receive the loan or have a limit set up. Every network interaction below passes through ONDC Tunnel. Steps inside the lender's environment (KYC, e-mandate, lien marking, eSign) happen outside the network, so Tunnel sees them only through the status updates the lender sends. The journey consists of the following stages:

### 1. Loan Application and Portfolio Discovery

The borrower provides their basic information through the Lending App (LSP), including:

- User type — Individual or Sole Proprietorship firm
- PAN, full name, gender, date of birth / date of incorporation
- Employment type (for individuals), annual income
- Mobile number, email ID, address, pincode, city, state
- End use of the loan
- Bureau consent

PAN, mobile number, and bureau consent should be validated particularly carefully — they gate identity matching, OTP-based flows, and any credit check downstream. DOB/DOI validation should branch by user type: an individual needs a DOB and age-eligibility check, while a sole-prop firm needs a DOI and possibly a firm-vintage check.

Alongside this, the LSP uses MF Central (or an equivalent aggregator) to pull the borrower's MF portfolio and broadcasts that portfolio — normalized scheme codes, AMC identifiers, unit counts, and NAV as of pull time — to participating lenders as part of the search request.

**Network interaction:**

- **`/search`**: The LSP sends the borrower's applicant details and MF portfolio data to participating lenders.
- **`/on_search`**: Participating lenders respond with their available LAMF products for this portfolio, including supported AMCs/schemes, eligible units, loan type, and pricing.

> **NAV Time Sensitivity**: NAV is time-sensitive. The LSP should track the as-of timestamp of the pulled portfolio data and be prepared to refresh it if the borrower's journey spans enough time that valuations could have materially moved — this matters again at the margin-call stage later.

> **On Tunnel**: The LSP sends one `/search` to the Tunnel endpoint, and Tunnel forwards it only to lenders whose portal declarations allow this LSP. Which lenders respond is set by declarations, not by a list in the LSP's code, so a lender missing from the offer set should be checked against the portal first. A `/search` that fails schema validation reaches no lender — the LSP should show this as a retryable error, not as "no offers available".

### 2. Loan Offers

Based on the portfolio shared, each lender returns an offer that may include:

- Supported AMCs/schemes, based on that lender's RTA tie-ups
- Eligible units from the borrower's portfolio — not necessarily the full portfolio, only units the lender can lend against
- Loan type: a Term Loan, or a limit (revolving or non-revolving)
- ROI, tenure, processing fee, and other KFS (Key Fact Statement) terms
- Loan amount

The LSP presents these offers for comparison.

Because "eligible units" is lender-specific, two lenders looking at the same portfolio can legitimately return different eligible-unit sets and different loan amounts. The offer comparison UI should make this visible rather than implying every lender evaluated the same collateral base. Revolving vs. non-revolving limit is also a meaningful structural difference for the borrower and should be a clearly labeled attribute, not buried in fine print.

> **On Tunnel**: Each lender's `/on_search` is validated before it reaches the LSP. An offer that fails validation never appears in the comparison, so lenders should monitor Tunnel rejections of their `/on_search` responses rather than assume every offer was delivered.

### 3. Offer Selection and Pledge Adjustment

The borrower can reduce the units they're willing to pledge, or deselect entire AMCs from consideration, before making a final selection. Every such change should trigger a full requote rather than an in-place adjustment — loan amount, ROI, and even loan-type eligibility can all change when the eligible collateral base shrinks. The LSP should also prevent a borrower from selecting a stale offer generated before their most recent pledge-set change.

**Network interaction:**

- **`/select`**: The LSP sends the selected loan product, along with the borrower's confirmed pledge selection.
- **`/on_select`**: The lender responds with the applicable loan quote — APR, processing fees, terms — and the link to continue the loan processing journey.

> **On Tunnel**: `/select` and `/on_select` are schema-validated, but validation does not catch a stale offer or a pledge set that no longer matches the quote. The stale-offer guard stays with the LSP, and the lender should still check the confirmed pledge set against what it quoted.

### 4. Lender Onboarding, Mandate Setup, and Pledge (Lien Marking)

After the borrower selects an offer, the borrower proceeds to the lender's onboarding journey, which is rendered within the LSP experience (app-in-app experience). The lender determines and executes the required steps, which may include:

- **KYC**: Digital or video KYC, per the lender's process.
- **e-Mandate**: Setup of the repayment mandate.
- **Lien marking**: The lender triggers a lien on the pledged units, via the CAMS/KFintech RTA API for folio-held units or via NSDL/CDSL for demat-held units.
- **eSign**: Digital execution of the loan agreement.

The lender communicates the status of these activities to the LSP through asynchronous `/on_status` updates.

**Network interaction:**

- **`/init`**: The LSP submits the borrower's KYC form to begin the lender's onboarding sequence.
- **`/on_init`**: The lender acknowledges and, as each onboarding step completes, pushes progress via `/on_status`.

> **Operational Point of No Return**: Treat lien marking as the operational point of no return in this journey — once marked, the borrower's ability to transact on those units is restricted until closure or release. If a borrower drops off mid-journey, or the lender needs an extra verification layer, the lender can initiate a data pull via CAMS/KFintech before pledge initiation — verification should be front-loaded ahead of lien marking wherever possible, precisely because lien marking shouldn't be triggered on an application that might still fail verification.

> **On Tunnel**: `/init`, `/on_init`, and every `/on_status` pass through Tunnel; the onboarding steps themselves do not. The network observability dashboard can show only the progress a lender reports, so lenders should send an `/on_status` at each completed step. A lender that reports only at the end leaves the network blind between `/on_init` and `/confirm`.

### 5. Loan Confirmation, Disbursal, and Limit Setup

Once KYC, mandate setup, lien marking, and agreement signing are complete, the LSP confirms the booking.

**Network interaction:**

- **`/confirm`**: The LSP submits the signed loan agreement and confirms the booking.
- **`/on_confirm`**: The lender validates the completed journey and confirms. For a Term Loan, funds are disbursed to the borrower's account. For a limit product, the operational limit is set up — available for drawdown, not transferred upfront.

### 6. Application Status and Offline Processing

Throughout the journey, the lender sends asynchronous `/on_status` updates so the LSP can track progress without managing the lender's internal processing.

Some lenders may require manual verification or processing that can't be completed digitally — a field visit, a branch check, a telephonic verification. In that case, the lender sends an `/on_status` update marking the application `IN_PROGRESS` with processing continuing offline, followed by a further `/on_status` update once that offline activity completes: `SUCCESSFUL` (the application proceeds with remaining digital steps) or `FAILED` (rejected, with rejection information). The LSP uses these updates to keep the borrower informed either way — this is a normal path, not an error state.

---

## Additional Scenarios

Servicing begins once a limit is set up or a term loan is disbursed. Everything that happens afterward — drawdowns, margin calls, payments, part-payments, enhancement, and foreclosure — is a servicing flow.

> **Platform-Maturity Note**: Lenders are not mandated to expose APIs for every servicing flow in this first phase — that requirement is expected once the product stabilizes. Build the LSP's servicing layer assuming a mixed reality at launch: some lenders may support status-update APIs, others may rely purely on redirection with manual dashboard refresh.

> **On Tunnel**: Servicing API calls (`/status`, `/update`, `/on_update`) pass through Tunnel and are validated like journey calls. Servicing done purely by redirection happens outside the network, so the network observability dashboard shows complete servicing activity only for lenders that use the servicing APIs.

### 1. Dashboard Retrieval

The LSP periodically queries the lender for current account status and displays it to the borrower.

**Network interaction:**

- **`/status`**: The LSP requests the current state of the loan or limit account.
- **`/on_status`**: The lender returns the account summary — sanctioned limit, current utilisation, available limit, and applicable fees.

Since API coverage isn't guaranteed uniformly across lenders in this phase, polling cadence and fallback behavior (e.g., "last updated at X" messaging) should be designed defensively rather than assuming real-time accuracy is always available.

### 2. Processing Fee (PF) Deduction

Lenders may use any of four methods to collect the processing fee, and a given lender may only support one:

1. **Upfront payment**: The borrower pays the PF directly within the lender's environment during the journey.
2. **Deducted from the assigned limit**: e.g., a ₹1,00,000 loan amount with a ₹2,000 PF results in the borrower seeing ₹98,000 available in their OD account.
3. **Deducted from the first drawdown**: e.g., a ₹1,00,000 assigned limit with the borrower's first drawdown of ₹50,000 nets them ₹48,000 after the ₹2,000 PF is taken out of that specific transaction.
4. **Bundled into the first month-end mandate**: e.g., ₹150 of accrued interest plus ₹2,000 PF results in a ₹2,150 mandate presentation at month-end.

Because the deduction method is lender-specific and changes what number the borrower actually sees at each step, the LSP should surface which method applies for a given lender clearly, rather than showing a generic "loan amount" figure that might not match what the borrower actually receives.

### 3. Drawdown

Applicable to limit-based (OD) products, where the borrower draws funds against a sanctioned limit rather than receiving a lump sum upfront.

**Network interaction:**

- **`/update` — `DRAW_DOWN` (on the Base Order)**: The borrower requests a drawdown against the available limit.
- **`/on_update` — approved terms, consent required**: The lender assesses collateral sufficiency and borrower performance, then returns approved drawdown terms and requests borrower consent.
- **`/update` — consent submitted**: The borrower confirms the terms.
- **`/on_update` — child order created, disbursement initiated $\rightarrow$ drawdown completed $\rightarrow$ base order updated**: The lender creates a child order for this specific drawdown, disburses, and finally updates the base order's utilisation to reflect the new draw. If the lender rejects the drawdown instead — at either the terms or the consent stage — it returns `/on_update` with rejection details in place of the success sequence.

If margin is insufficient for the requested amount, the lender may return a reduced eligible amount instead of a flat rejection. The drawdown flow needs a confirm-at-a-different-amount step for this — "you asked for X, you're eligible for Y, confirm Y?" — not just an accept/reject binary.

### 4. Limit Enhancement

The borrower requests a credit limit increase; the lender evaluates eligibility and collateral via redirection, then either approves a higher limit — which may come with new pledge requirements — or rejects the request. The LSP displays the outcome and refreshes the dashboard.

Because enhancement can require additional units to be pledged, this flow should loop back into something resembling the offer-selection/pledge-adjustment logic from [Offer Selection and Pledge Adjustment](#3-offer-selection-and-pledge-adjustment), not be treated as a simple numeric limit bump.

### 5. Interest / EMI Payment and Missed-Interest Payment

Interest typically accrues daily, with lenders following a monthly presentation cycle. Borrowers are usually given a short window to pay voluntarily; if they miss it, a mandate is presented against the borrower's repayment account at the end of that window — these are two distinct payment paths with different status transitions and different borrower-facing messaging needs.

**Network interaction (missed interest):**

- **`/update` — `MISSED_INTEREST_PAYMENT` (on the Child Order)**: The borrower requests payment details for interest that wasn't collected through the mandate.
- **`/on_update` — quote $\rightarrow$ success $\rightarrow$ base order updated**: The lender returns the outstanding interest, penal charges, and a payment link; once paid, confirms success and updates the base order.

### 6. Part-Payment (Partial Principal)

**Network interaction:**

- **`/update` — `PRE_PART_PAYMENT` (on the Child Order)**: The borrower requests to prepay part of the outstanding principal.
- **`/on_update` — quote $\rightarrow$ success $\rightarrow$ base order updated**: The lender returns the applicable amount and charges; once paid, adjusts the outstanding principal and updates pledge requirements if any units can now be released.

A part-payment can trigger a partial lien release, which loops back into RTA/depository coordination — this isn't purely a balance update on the lender's ledger.

### 7. Foreclosure (Full Loan Closure)

**Network interaction:**

- **`/update` — `FORECLOSURE`**: The borrower requests full closure of the loan.
- **`/on_update` — foreclosure quote $\rightarrow$ foreclosure success**: The lender returns the total foreclosure amount — outstanding principal, accrued interest, and charges — then confirms once payment is received and releases the lien on all pledged units.

Closure should be treated as complete only once lien release is confirmed, not merely once the payment clears — the borrower's practical goal is getting their units back to freely transact, which depends on the release, not just the payment. The lender is responsible for calculating and disclosing applicable foreclosure/prepayment charges; for certain floating-rate personal loans to individual borrowers, RBI regulations restrict the levy of such penalties.

### 8. Margin Calls and Liquidation

**Network interaction:**

- **`/on_update` — `MARGIN_CALL_RAISED` (unsolicited)**: When pledged-unit value falls, or utilisation rises relative to the required margin, the lender sends an unsolicited margin call specifying the shortfall amount, a due date (commonly seven days), and a redirection URL for the borrower to cure it.
- **`/on_update` — `MARGIN_CALL_RESOLVED` or `MARGIN_CALL_EXPIRED`**: The lender marks the margin call resolved once the shortfall is cured, or expired if the due date lapses without resolution.
- **`/on_update` — `LIQUIDATION_COMPLETED` (unsolicited)**: If the margin call expires, the lender liquidates enough pledged units to cover the shortfall and notifies the LSP with units sold, amount recovered, and updated limit — linked back to the originating margin call.

This is the highest-stakes flow in the product. Margin calls are lender-initiated and unsolicited from the LSP's perspective, so the LSP needs a push/webhook-style ingestion path (or frequent polling) specifically for this event — it cannot be something the borrower only discovers by opening the dashboard. The due-date window is short relative to other flows in this journey, so notification latency directly eats into the borrower's remedy window; this path should be prioritized for reliability over other servicing notifications. Liquidation is irreversible and involuntary from the borrower's standpoint — post-liquidation messaging should be unambiguous about what was sold, what was recovered, and what the borrower's resulting position is, since this is the moment most likely to generate a grievance.

> **On Tunnel**: Margin-call and liquidation messages pass the same schema validation as every other call. A `MARGIN_CALL_RAISED` that fails validation is rejected at Tunnel and never reaches the LSP, while the borrower's cure window keeps running. Lenders should treat a Tunnel rejection on this message as an incident and resend at once, ahead of any other servicing fix. Tunnel's logs also give a network-side record of when each margin call passed through the network, which matters if a borrower later disputes notice.

---

## Issue and Grievance Management

A borrower can raise a grievance through the LSP for issues related to their loan or the network transaction. The LSP routes the grievance to the relevant lending partner through the network's grievance mechanism. The lender is responsible for investigating and resolving the grievance and communicates status and resolution back to the LSP, which makes that information available to the borrower.

IGM handling is standardized across FIS12, so an LSP or lender that has already implemented IGM for another FIS12 lending product should be able to reuse that implementation for LAMF rather than building a separate grievance pipeline.

Given that the margin-call/liquidation flow is the most likely source of borrower disputes, the IGM integration should be tested specifically against that scenario — e.g., "units were liquidated but I didn't receive or see the margin call in time" — rather than only against generic servicing complaints.

> **On Tunnel**: For that dispute, the first question is where the margin call stopped — never sent, rejected at Tunnel, or delivered to the LSP but not shown to the borrower. Tunnel's network-side logs can help answer this without each side reconciling its own logs first.

---

## Figma

[View Figma Board](https://www.figma.com/design/pF6i0CqlqkBheLtQTYNBW6/Untitled?node-id=0-1&p=f)
