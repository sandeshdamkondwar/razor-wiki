---
title: Collect Convenience Fees on International Payments
desc: Charge convenience fees on international payments.
index: false
---

For every international payment done using Razorpay, we levy a nominal platform fee. You can choose to charge a Convenience Fee to your international customers for the use of technology infrastructure. Using the Convenience Fee Model, you can allow customers to pay in their native or any other currency and view the applicable Convenience Fee on the Checkout page.

<callout info>

**Handy Tips**

This feature is currently supported for specific business cases only. You can contact our <a href="https://razorpay.com/support/">Support team</a> to get this feature enabled on your account.
</callout>

# How it Works

Given below is the workflow:

1. You log in to the <a href="https://dashboard.razorpay.com/" target="_blank">Razorpay Dashboard.</a>
2. You select the **Convenience Fee Model** option on the **Settings → Fee Bearer** section of the Razorpay Dashboard.
3. The customer selects an item on your website/Payment Link/Payment Page and clicks **Pay** button.
4. The checkout pop-up page is displayed. The customer enters the **Phone number and Email**.
    <img src="/docs/assets/images/cfb-dcc-phone-no-details.jpg" alt="customer details" width="800"/>

5. The customer selects the payment method on the checkout page and tries to make the payment.
    <img src="/docs/assets/images/cfb-dcc-card-details.jpg" alt="card details" width="800"/>

6. The customers also get the option to change the currency as per their choice. Based on the selected currency, the **Fees Breakup** page containing the **Convenience Fee** appears, and the customer clicks **Continue**.
    <img src="/docs/assets/images/cfb-dcc-charges-breakup.jpg" alt="Fees breakup" width="800"/>

7. The customer is redirected to the bank page with the total amount, including the Convenience Fee.

## Reports

Convenience Fees on international payments will reflect on all the reports in the same format as on the checkout. The charge is added to the total amount in the reports. Reports can be generated from the <a href="https://dashboard.razorpay.com" target="_blank">Razorpay Dashboard</a> under the **Reports** tab.

## Communication

You should inform the customers about the Convenience Fee on international payments. We do not notify the customers of the Convenience Fee except at checkout. In the Razorpay Payment Acknowledgement email on successful payment, the Convenience Fee are added to the total amount.

## Frequently asked questions (FAQs)

#### 1. What is a customer fee bearer or Convenience Fee model?
For every payment done using Razorpay, we levy a nominal platform fee. You can choose to charge a Convenience Fee from customers, which is called the Convenience Fee model.
 
#### 2. How does Razorpay collect Convenience Fee from the customer?
Convenience Fees are seamlessly added on the Razorpay Checkout without disrupting the checkout experience for the customers.

#### 3. Which all currencies are supported?
Refer to the <a href="/docs/payments/payments/international-payments#supported-currencies" target="_blank">list of currencies </a> that support the Convenience Fee model.

#### 4. How to enable this feature?
Follow these steps to enable the feature:
1. Log in to the Razorpay Dashboard.
2. Navigate to Settings → Configurations.
3. Select the Convenience Fee Model option in the Fee Bearer section.

#### 5. How does a refund work? 
If a refund is initiated, your customers receive the Convenience Fees and the actual payment amount.

#### 6. Do I qualify for such a feature? 
This feature is supported for most international businesses on Standard Checkout, provided they meet the necessary business requirements. You can contact our <a href="https://razorpay.com/support/" target="_blank" >Support team</a> to get this feature activated on your account.
However, if your account has PayPal enabled, this feature will not be supported.

#### 7. What all payment methods are supported?
We support this feature on the following methods:
- International debit / credit cards
- Instant bank transfer (Trustly, Poli, Sofort and Giropay)
- We do not support Paypal on Convenience Fee bearer as Razorpay does not charge any platform fee for PayPal transactions. Hence this fee can not be passed on to customers from Razorpay.

#### 8. Which integrations are supported? 
Currently, this feature is available on Standard Checkout only.


## Related Information

- <a href="/docs/payments/dashboard/settings/configuration/convenience-fees/" target="_blank">Convenience Fee Model</a>
- <a href= "/docs/payments/payments/international-payments/" target="_blank">International Payment Support</a>
