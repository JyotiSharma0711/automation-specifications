# ONDC Credit Card Applications: Consumer Cards for Individuals

- [Scope](#scope)
- [Participants](#participants)
- [Requirements](#requirements)
  - [1 – Registration and Onboarding](#1--registration-and-onboarding)
  - [2 – Fetching Preliminary Information for Underwriting](#2--fetching-preliminary-information-for-underwriting)
    - [2.1 – Preliminary Applicant Information for Card Underwriting](#21--preliminary-applicant-information-for-card-underwriting)
    - [2.2 – Consent to Share Applicant's Information with Issuers](#22--consent-to-share-applicants-information-with-issuers)
    - [2.3 – Broadcasting Applicant's Information to Issuers](#23--broadcasting-applicants-information-to-issuers)
  - [3 – Consumer Card Underwriting and Making the Offer](#3--consumer-card-underwriting-and-making-the-offer)
  - [4 – Selecting a Consumer Card](#4--selecting-a-consumer-card)
    - [4.1 – Eligible and Satisfied with Card Offerings](#41--eligible-and-satisfied-with-card-offerings)
    - [4.2 – Eligible but Not Satisfied with Card Offerings](#42--eligible-but-not-satisfied-with-card-offerings)
    - [4.3 – Not Eligible for Any Card Offerings](#43--not-eligible-for-any-card-offerings)
  - [5 – Card Application: KYC Verification](#5--card-application-kyc-verification)
    - [5.1 – KYC Documentations](#51--kyc-documentations)
    - [5.2 – Other KYC Steps](#52--other-kyc-steps)
  - [6 – Card Application Completion](#6--card-application-completion)
    - [6.1 – Consumer Card Agreement](#61--consumer-card-agreement)
    - [6.2 – Consumer Card Fulfilment](#62--consumer-card-fulfilment)
    - [6.3 – Consumer Card Management](#63--consumer-card-management)

---

## Scope

The scope of this document is to create API specifications for the ONDC Financial Services network, focusing on consumer credit products, specifically consumer card applications. This will provide applicants access to a pre-approved credit line and the convenience of making payments.

The primary use cases are:

1. Supporting the fetching of all documents required for a consumer card application and applying to issuers.
2. Enabling issuers to offer attractive consumer cards for applicant acknowledgement and agreement.

---

## Participants

| Participant | Description/Role |
|---|---|
| **Issuers** | RBI-registered 'Regulated Entities', such as Scheduled Commercial Banks (SCBs), Non-Banking Financial Companies (NBFCs), Primary (Urban) Co-operative Banks (UCBs), and Regional Rural Banks (RRBs). |
| **Buyer Apps** | Any application that adheres to prevailing guidelines issued by RBI. |
| **Applicant** | Individuals looking to apply for a consumer credit card. |
| **Third Party Data Providers** | Data providers who provide derived or direct data from sources such as MCA. |
| **Account Aggregators (AA) or equivalent bank data providers** | Data providers who have secure means of collecting, analyzing and transmitting key banking indicators. Examples include Perfios and Corpository. |
| **RBI regulated Credit Information Companies** | To provide applicant's credit history. An example is TransUnion CIBIL. |

---

## Requirements

### 1 – Registration and Onboarding

Primary users of the buyer application (referred to as "buyer app") are applicants seeking consumer cards. The applicant registers on the buyer app by entering the following details:

1. Email
2. First and last name
3. Mobile number, validated with an OTP, and on every new login

The buyer app then presents the applicant with various financial services and products. For this use case, we focus on consumer card applications.

When the applicant opts to explore consumer cards, the buyer app sends a search request to the ONDC Gateway to lookup the list of issuers offering consumer cards. The ONDC Gateway queries the relevant registry of card issuers and forwards the search request to each issuer. Each interested issuer then sends their static catalog to the buyer app endpoint.

### 2 – Fetching Preliminary Information for Underwriting

The buyer app requests the applicant for:

- Applicant's preliminary information required for basic card underwriting (see [2.1](#21--preliminary-applicant-information-for-card-underwriting))
- Consent to retrieve the applicant's information from a third-party provider (see [2.2](#22--consent-to-share-applicants-information-with-issuers))

The information collected are as follows:

- Personal details: PAN, first name, last name, sex, date of birth
- Contact information: mobile number, email, residential address
- Employment details: employment status, gross annual income
- Declarations: political exposed persons, conflicts of interest
- Data pull consent: bureau consent

#### 2.1 – Preliminary Applicant Information for Card Underwriting

This can be collected via:

**a. Pre-filling standardized form via bureau pull**

1. The applicant shares their PAN and mobile number on the buyer app.
2. The buyer app obtains consent to retrieve the applicant's bureau data via a soft pull and subsequently share the information retrieved to issuers.
3. The buyer app verifies the mobile number with an OTP and obtains data and credit history access authorization from the bureau (e.g. TransUnion CIBIL) through OTP verification on the number linked to the PAN.
4. The buyer app retrieves information required via the soft pull and displays it to the applicant for confirmation.
5. If retrieval from a third-party provider is not possible or there are gaps in the information, the applicant manually inputs the missing information into the form.

**b. Manually filling up standardized form and obtaining bureau pull consent**

Alternatively, the buyer app prompts the applicant to complete a standardized form that includes consent for a bureau pull. This consent is then forwarded to issuers to complete the consumer card underwriting process.

#### 2.2 – Consent to Share Applicant's Information with Issuers

Due to the importance of data security, the buyer app must obtain explicit consent from the applicant to collect and share their information with issuers to generate consumer card offers.

#### 2.3 – Broadcasting Applicant's Information to Issuers

The buyer app broadcasts the applicant's information to each issuer that responded to the initial search request, using the endpoints provided in their static catalog.

### 3 – Consumer Card Underwriting and Making the Offer

Each issuer evaluates the applicant's profile using their business rules and returns a catalog of relevant consumer card offers to the buyer app. A maximum of two card offers may be produced by issuers in any single offer catalog. The buyer app then collates and displays all offers to the applicant.

### 4 – Selecting a Consumer Card

#### 4.1 – Eligible and Satisfied with Card Offerings

The applicant browses the list and reviews the card features and terms and conditions. Card highlights include joining and annual fee, rewards scheme and card benefits. They can click on each card for more details. The applicant then selects their desired consumer card and submits the applications request.

#### 4.2 – Eligible but Not Satisfied with Card Offerings

If unsatisfied with the card offerings, the applicant may choose to regenerate offers by providing additional documentation to prove creditworthiness. (Refer to steps below for collecting bank statements.) After submitting the required documents, the applicant can click to regenerate offers. This repeats the process of sending their information to each interested issuer (see [2](#2--fetching-preliminary-information-for-underwriting)), consumer card underwriting and offer generation (see [3](#3--consumer-card-underwriting-and-making-the-offer)).

**a. Obtain bank statements via account aggregators (AAs)**

1. The buyer app requests the applicant to select their primary bank, enabling the selection of supported account aggregators (AAs) from a comprehensive list.
2. The buyer app requests the applicant to create consent requests at the account aggregator, providing the AA identifier (AA ID) of the applicant in the format of `{mobile_number}@{aa_name}`.
3. The applicant responds with consent handles, a unique ID identifying a particular consent at the AA.
4. The buyer app redirects the applicant to the chosen AA, where they can review and either approve or decline the consent requests.
5. Once the applicant approves the data pull consent, the AA notifies the issuer(s), who can then retrieve the applicant's bank account statements.

**b. Manual upload of required documents**

The buyer app includes an option for applicants to securely upload their bank statements.

#### 4.3 – Not Eligible for Any Card Offerings

However, if the applicant is not eligible for any card variant, the buyer app can suggest and redirect them to collateral-based card applications.

### 5 – Card Application: KYC Verification

Upon receiving offer acceptance from the buyer app, the issuer initiates the KYC process if required. The buyer app presents available options to complete the KYC.

#### 5.1 – KYC Documentations

The buyer app must allow document uploads and provide options for applicants to retrieve their documents via third-party providers (e.g., AAs). KYC documents typically expected include:

- Proof of identity: PAN card, Aadhaar card, or passport
- Proof of address: Aadhar card, or recent utility bill
- Proof of income: income tax return (ITR), or pay slip (if applicant is a salaried employee)

#### 5.2 – Other KYC Steps

The buyer app should facilitate the completion of digital KYC steps (e.g., video KYC) within its interface by integrating the issuer's KYC link to provide an in-app experience. This enables a seamless consumer card application process.

Any non-digital KYC steps will be completed separately and out-of-band.

### 6 – Card Application Completion

#### 6.1 – Consumer Card Agreement

The issuer shares the consumer card agreement with the applicant through the buyer app. The applicant signs it using either clickwrap OTP or Aadhar eSign. The consumer card application is then complete.

#### 6.2 – Consumer Card Fulfilment

The issuer is responsible for card fulfillment, including delivering the physical card or providing card information for digitization. During this process, the status of card fulfillment should be reflected on the buyer app, along with other details such as the expected delivery date.

#### 6.3 – Consumer Card Management

After the consumer card is delivered and activated, the buyer app displays relevant card information, including:

- Available credit limit: available cash advance limit and overall credit limit
- Payment details: outstanding balance, statement balance, statement date, minimum amount payable and payment due date
- Card details: card name, card number and expiry date

The buyer app also provides steps for applicants to repay their credit dues through a payment link.
