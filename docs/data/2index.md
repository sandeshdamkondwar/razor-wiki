---
title: Collect Convenience Fees from Customers
desc: Collect convenience fees from your customers for using your technology and infrastructure.
index: false
tree: |
    index

---

For every payment done using Razorpay, we levy a nominal platform fees. You can choose to charge a Convenience Fee to your customers for the use of technology infrastructure. Convenience Fees are seamlessly added at Razorpay Checkout without disrupting the checkout experience for your customers. In case a refund is initiated, your customers receive the Convenience Fees along with the actual payment amount.

<img src="/docs/assets/images/dashboard-guide-settings-fee-bearer-fee-breakup.jpg" alt="Fees breakup" width="300"/>

<callout info>
**Handy Tips**

- This feature is currently supported for specific business cases only. You can contact our <a href="https://razorpay.com/support" target="blank">Support team</a> to get this feature activated on your account.
- **INR** is the only supported currency. This feature is not available for international payments.
- This feature is **not available** for:
    - Smart Collect (via VA, VPA and QR Codes)
    - Route
    - Subscriptions (via Emandate, Paper NACH)
</callout>

# How it Works

Given below is the workflow:



1. Log in to the <a href="https://dashboard.razorpay.com/" target="_blank">Razorpay Dashboard</a>.
2. You select the **Convenience Fee Model** option on the **Settings** → **Fee Bearer** section of the Razorpay Dashboard.

    <img src="/docs/assets/images/dashboard-guide-settings-fee-bearer-customer-fee-bearer.jpg" alt="Customer pays the fee" width="600"/>
3. The customer selects an item on your website/Payment Link/Payment Page and clicks the pay button.
    <img src="/docs/assets/images/dashboard-guide-settings-fee-bearer-payment-page.jpg" alt="Customer clicks pay button" width="600"/>
4. The checkout pop-up page is displayed.
    <img src="/docs/assets/images/dashboard-guide-settings-fee-bearer-checkout-new1.jpg" alt="checkout form" width="300"/>
5. The customer selects the payment mode and clicks the **Pay** button.
6. The **Fees Breakup** page containing the Convenience Fee appears, and the customer clicks **Continue and pay**.
    <img src="/docs/assets/images/dashboard-guide-settings-fee-bearer-fee-breakup-new1.jpg" alt="Fees breakup" width="300"/>
7. The customer is redirected to the bank page with the total amount, including the Convenience Fee.


<callout info>
**Handy Tips**

Convenience Fees are collected in a similar fashion at Custom UI Checkout and Hosted Checkout.
</callout>

# Reports

Convenience Fees reflect on all the reports in the same format as on the checkout. The charge is added to the total amount in the reports. Reports can be generated from the <a href="https://dashboard.razorpay.com" target="_blank">Razorpay Dashboard</a> under the **Reports** tab.

# Communication

You should inform the customers about the Convenience Fees. We do not notify the customer of the Convenience Fees except at checkout. In the Razorpay Payment Acknowledgement email on successful payment, the Convenience Fees are added to the total amount.

<callout warn>
**Watch Out!**

The email does not contain the payment breakup to indicate the Convenience Fees separately but is added to the total amount.
</callout>
