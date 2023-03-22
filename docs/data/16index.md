---
title: Balances 
desc: Know about the various balances available to you and how you can add funds and maintain to each of them from the Dashboard.
index: false
tree: |
  index | Balances
---

There are two types of balances available to you [Current Balance](#current-balance) and [Reserve Balance](#reserve-balance).
<img src="/docs/assets/images/balance-overview.jpg" class="click-zoom" width="600" alt="Balances Overview"/>


<show-if org="razorpay">

# Current Balance

After deduction of fees and tax, the payments received from your customers are added to your Merchant Balance or Current Balance. This accumulated amount is settled in your bank account according to your settlement cycle.
- The current balance is used to process refunds to your customer, settlements to your linked accounts and chargebacks.
- It is important for you to  maintain a sufficient current balance. You can [add funds to your current balance](#add-funds-to-your-current-balance) account from your Dashboard to ensure you have sufficient current balance for your business needs.
- We do not charge any fee to process refunds. However, the fees and tax charged for processing the original transaction are not refunded to you when you process a customer refund. This amount is deducted from your current balance when you process your refund.

## Add Funds to your Current Balance

Watch this video to know how to add funds to your current balance.

<iframe width="560" style='max-width:100%' height="315" src="https://www.youtube.com/embed/ol6HV7KxnP0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

To add funds to your current balance:

1. Log in to the <a href="https://dashboard.razorpay.com/#/access/signin" target="_blank">Razorpay Dashboard</a>.
1. Navigate to **My Account** → **Balances**.
1. Click **Add Funds** in the Current Balance section and follow the on-screen instructions.

<callout info>
**Handy Tips**

When you add funds to your current balance, fees and tax are deducted and the remaining amount is added to your current balance. The fees and tax charged are the same as what is charged on payments received from customers.

For example, according to your pricing plan for a ₹1,000 payment, the fees and tax is ₹5. When you add ₹1,000 to your current balance, ₹5 (fees and tax) is deducted from it and ₹995 is added to your current balance.
</callout>

### Example 1

Let us say you have a current balance of ₹1,000.

<table>
| Current Balance
---
Opening balance | ₹1,000
---
You receive and capture a payment of ₹1,000.<br/><br/>Let us assume we charge a fee of ₹5 to process this transaction. | ₹1995<br/><br/>(₹1,000 + (₹1,000 - ₹5))
---
You process a full refund of ₹1,000 for the above payment. | ₹995<br/><br/>(₹1995 - ₹1,000)
</table>

### Example 2

Let us say you have a current balance of ₹0.

<table>
| Current Balance
---
Opening balance | ₹0
---
You receive and capture a payment of ₹1,000.<br/><br/>Let us say a fee of ₹5 is charged by us to process this transaction. | ₹995<br/><br/>(₹0 + (₹1,000 - ₹5))
---
You try process a full refund of ₹1,000 for the above payment. | The refund fails since you do not have sufficient current balance.
</table>

# Reserve Balance

Reserve Balance allows you to process refunds or settlements to linked accounts even if you do not have a sufficient current balance. The amount you add as the reserve balance becomes the maximum negative limit for your account. Razorpay does not deduct funds from your reserve balance. It uses the reserve amount as a negative limit for your account balance.

### Example 1

If you add ₹1000 to your reserve balance, the negative limit of your account balance is automatically set at -1000. This means, in case you do not have sufficient current balance, Razorpay will not fail your transactions till this limit is breached.

You can [add funds to your reserve balance from the Dashboard](#add-funds-to-your-reserve-balance) to increase your negative balance limit. In most cases, you will have to transfer funds to your reserve balance only once.


## Add Funds to your Reserve Balance

You can add funds to Reserve Balance using the Razorpay Dashboard through either [UPI](#add-funds-to-your-reserve-balance-through-upi) or [Bank Transfer](#add-funds-to-your-reserve-balance-through-bank).

<callout warn>
**Watch Out!**

Addition of funds should be done only through the settlement account registered with us.
</callout>

Watch this video on how to add Funds to your Reserve Balance.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3QgUy4BUNc4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Add Funds to your Reserve Balance through UPI:

1. Log in to the <a href="https://dashboard.razorpay.com/" target="_blank">Razorpay Dashboard</a>.
2. Navigate to **My Account** → **Balances**.
3. Click **Add Funds**.
    <img src="/docs/assets/images/reserve-balance.jpg" class="click-zoom" width="500" alt="Add Reserve balance"/>
4. Select **UPI**.
    <img src="/docs/assets/images/upi-only.jpg" class="click-zoom" width="300" alt="Select UPI"/>
4. Enter the description and amount to be added.
5. Click **Add Credits**.
    <img src="/docs/assets/images/add-reserve-funds.jpg" class="click-zoom" width="300" alt="Add Reserver Balance Funds"/>
6. Enter the email and contact number on the checkout pop-up page, select UPI, and complete the payment.
    <img src="/docs/assets/images/balance-add-contact-email.jpg" class="click-zoom" width="300" alt="Add number and email.jpg"/>
Your Reserve Balance is updated.

<callout info>
**Handy Tips**

It may take 2-3 hours for the Reserve Balance to reflect in your Razorpay Account.
</callout>


### Add Funds to your Reserve Balance through Bank Transfer:
1. Log in to the <a href="https://dashboard.razorpay.com/" target="_blank">Razorpay Dashboard</a>.
2. Navigate to **My Account** → **Balances**.
3. Click **Add Funds**.
    <img src="/docs/assets/images/reserve-balance.jpg" class="click-zoom" width="500" alt="Add Reserve balance"/>
4. Select **Bank Transfer**.
    <img src="/docs/assets/images/upi-only.jpg" class="click-zoom" width="400" alt="Select UPI and Netbanking"/>
5. Copy the account number and IFSC code.
    <img src="/docs/assets/images/copy-ifsc.jpg" class="click-zoom" width="300" alt="Copy IFSC and account number"/>
6. Open your netbanking portal, create a beneficiary with these details and transfer the amount.

<callout info>
**Handy Tips**

It may take 2-3 hours for the Reserve Balance to reflect in your Razorpay Account.
</callout>

# Example of Current Balance and Reserve Balance

Let us say you have a current balance of ₹0 and a reserve balance of ₹1,000

<table>
| Without Reserve Balance | With Reserve Balance
---
Opening Balance | Current Balance → ₹0<br/>Reserve Balance → ₹0| Current Balance → ₹0<br/>Reserve Balance → ₹1,000
---
You receive and capture a payment of ₹1000.<br/><br/>Let us say a fee of ₹5 is charged by us to process this transaction. | Current Balance → ₹995<br/>Reserve Balance → ₹0| Current Balance → ₹995<br/>Reserve Balance → ₹1,000
---
You process a full refund of ₹1000 for the above payment. | The refund fails since you do not have sufficient current balance. | The refund is successfully processed.<br/><br/>Current Balance → negative ₹5<br/>Reserve Balance → ₹1,000
</table>

</show-if>

<show-if org="axis">


# Current Balance

The payments received from your customers, after deduction of fees and tax, is added to your Merchant Balance or Current Balance. This accumulated amount is settled to your bank account according to your settlement cycle.
- The current balance is used to process refunds to your customer, settlements to your linked accounts and chargebacks.
- It is important for you to  maintain a sufficient current balance. You can [add funds to your current balance]((#add-funds-to-your-current-balance)) account from your Dashboard to ensure you have sufficient current balance for your business needs.
- We do not charge any fee to process refunds. However, the fees and tax charged to process the original transaction are not refunded to you when you process a customer refund. This amount is deducted from your current balance when you process your refund.

## Add Funds to your Current Balance

To add funds to your current balance:

1. Log in to the <a href="https://axis.razorpay.com/" target="_blank">Dashboard</a>.
1. Navigate to **My Account** → **Balances**.
1. Click **Add Funds** in the Current Balance section and follow the on-screen instructions.

<callout info>
**Handy Tips**

When you add funds to your current balance, fees and tax are deducted and the remaining amount is added to your current balance. The fees and tax charged is the same as what is charged on payments received from customers.

For example, according to your pricing plan for a ₹1,000 payment, the fees and tax is ₹5. When you add ₹1,000 to your current balance, ₹5 (fees and tax) is deducted from it and ₹995 is added to your current balance.
</callout>


### Example 1

Let us say you have a current balance of ₹1,000.

<table>
| Current Balance
---
Opening balance | ₹1,000
---
You receive and capture a payment of ₹1,000.<br/><br/>Let us say a fee of ₹5 is charged by us to process this transaction. | ₹1995<br/><br/>(₹1,000 + (₹1,000 - ₹5))
---
You process a full refund of ₹1,000 for the above payment. | ₹995<br/><br/>(₹1995 - ₹1,000)
</table>

### Example 2

Let us say you have a current balance of ₹0.

<table>
| Current Balance
---
Opening balance | ₹0
---
You receive and capture a payment of ₹1,000.<br/><br/>Let us say a fee of ₹5 is charged by us to process this transaction. | ₹995<br/><br/>(₹0 + (₹1,000 - ₹5))
---
You try process a full refund of ₹1,000 for the above payment. | The refund fails since you do not have sufficient current balance.
</table>

# Reserve Balance

Reserve Balance allows you to process refunds or settlements to linked accounts even if you do not have a sufficient current balance. The amount you add as the reserved balance becomes the maximum negative limit for your account. Razorpay does not deduct funds from your reserved balance. It uses the reserved amount as a negative limit for your account balance.

### Example 1

If you add ₹1000 in your reserved balance, the negative limit of your account balance is automatically set at -1000. This means, in case you do not have sufficient current balance, Razorpay will not fail your transactions till this limit is breached.

You can [add funds to your reserved account from the Dashboard](#add-funds-to-your-reserve-balance) to increase your negative balance limit. In most cases, you will have to transfer funds to your reserved balance only once.

## Add Funds to your Reserve Balance

To add funds to your reserve balance:

1. Log in to the <a href="https://axis.razorpay.com/" target="_blank">Dashboard</a>.
1. Navigate to **My Account** → **Balances**.
1. Click **Add Funds** in the Reserve Balance section and follow the on-screen instructions.


# Example of Current Balance and Reserve Balance

Let us say you have a current balance of ₹0 and reserve balance of ₹1,000

<table>
| Without Reserve Balance | With Reserve Balance
---
Opening Balance | Current Balance → ₹0<br/>Reserve Balance → ₹0| Current Balance → ₹0<br/>Reserve Balance → ₹1,000
---
You receive and capture a payment of ₹1000.<br/><br/>Let us say a fee of ₹5 is charged by us to process this transaction. | Current Balance → ₹995<br/>Reserve Balance → ₹0| Current Balance → ₹995<br/>Reserve Balance → ₹1,000
---
You process a full refund of ₹1000 for the above payment. | The refund fails since you do not have sufficient current balance. | The refund is successfully processed.<br/><br/>Current Balance → negative ₹5<br/>Reserve Balance → ₹1,000
</table>

</show-if>


