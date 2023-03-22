---
title: Negative Balance for eMandate Registrations
desc: Know how you can maintain a negative balance limit in your Razorpay primary account balance so that the transactions involving the transfer of funds from your account never fail.
index: false
---

In situations where the debit transactions are more than your current balance, the transactions initiated from your account fail. To fill in the deficit of funds, you may have to <a href="/docs/payment-gateway/balances/dashboard" target="_blank"> add funds to your account</a> or <a href="/docs/payment-gateway/dashboard-guide/credits" target="_blank">upload fee credits</a>. To avoid such failures, Razorpay enables **Negative Balance** for your account so that you can allow transactions up to a certain amount below the current account balance without hindering your business.

# Use Cases

Following are a couple of use cases where the negative balance limit benefits your business:

**eMandate Registrations**
The customer registers for eMandate and makes the authorisation payment. The payment is captured. The MDR, that is, the transaction fees, is deducted from your balance, and the amount is settled to your account. This marks the mandate as successful.

In case of insufficient funds, the payment is in an authorised state and is not captured for a  time. The capture is unsuccessful as Razorpay is not able to deduct the transaction fees. You can neither refund the amount to the customer nor mark the mandate registration as complete.

With Negative Balance enabled for your account, a certain amount in your balance is used as **reserve** at all times. This amount is adjusted in a way that the transaction fees that Razorpay charges are accounted as a negative balance so that there are no interruptions in your eMandate registrations. The incoming transactions offset this negative balance.

## Notifications About Negative Balance

As per the threshold of negative balance set for your account, you receive notifications via email, SMS, or Dashboard announcements to add funds to your balance.  Following are the scenarios:

- When your Account Balance shows low funds.
- When the Negative Balance limit is more than the threshold.

<callout warn>
**Account Suspension**

If the negative balance in your account is for more than the maximum set time limit or the balance limit, your account is suspended immediately, and all the payouts are put on hold.
</callout>
