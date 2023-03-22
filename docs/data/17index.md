---
title: Negative Balance for Refunds and Route
desc: Know how you can maintain a minimum balance for cases of fund reversals from your account as in the case of refunds or transfer of funds to your linked accounts.
index: false
---

You can override the default negative balance limit set for your account so that the transactions that you initiate do not fail due to insufficient balance in your account. Your balance is moved to a negative value if the debit transaction value is more than the account balance. You should set a negative account balance limit to prevent the failure of fund transfers that you initiate. It is helpful in situations wherein the refund, or transfer amount is greater than the account balance. Your negative account balance is offset by the incoming transactions.

<callout info>
**Feature Enablement**
For configuring a negative balance limit for your account, contact our <a href="https://razorpay.com/support/#raise-a-request" target="_blank"> Support Team</a> or your account manager from Razorpay. As per Razorpay's set criteria, this feature is enabled for your account.
</callout>

# Use Cases
Following are a couple of use cases where the negative balance limit benefits your business:

## Transferring Funds to Linked Accounts
Let us say that you are an insurance aggregator and have received a payment of ₹100 from your customer. After standard deduction of MDR (including GST) of ₹2.18, Razorpay settles ₹97.82 to your account. Now, this payment has to be transferred, say ₹50, to each of your linked accounts (assuming that there are two of them). The linked accounts must receive the entire amount in full due to compliance.

If you have not set the negative balance limit for your account, transfers to one of the linked accounts will fail due to an insufficient balance(₹97.82-₹50=₹47.82). With a negative balance limit set, the TDR is managed with the negative balance so that the settlements to linked accounts do not fail.

## Refunds and Reversals
Let us say that you have received a payment of ₹100 from your customer on day `T`. This amount will be settled in your bank account on `T+2` day. Assuming that the customer has requested a refund on `T+3` day and your account balance is zero, the refund will fail. The same scenario is repeated in the case of fund reversals from the linked accounts.

You can complete the refund or fund reversals successfully if you have set a negative balance limit for your account.

## Notifications About Negative Balance

As per the threshold of negative balance set for your account, you receive notifications via email, SMS, or Dashboard announcements to add funds to your balance.  Following are the scenarios:

- When your Account Balance shows low funds.
- When the Negative Balance limit is reached.

<callout warn>
**Account Suspension**

If the negative balance in your account is for more than the maximum set time limit or the balance limit, your account is suspended immediately, and all the payouts are put on hold.
</callout>


