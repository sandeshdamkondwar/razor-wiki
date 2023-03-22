---
title: Configuration
desc: Manage notifications, Checkout themes, payment capture and more under the Configuration tab on the Razorpay Dashboard.
razorpay-MY-desc: Manage notifications, Checkout themes, payment capture and more under the Configuration tab on the Curlec Dashboard.
---
You can use the **Configuration** tab to perform the following operations:

<show-if org="razorpay" country="IN">

- [Change Checkout Theme](#change-checkout-theme)
- [Configure Email Address Field](#configure-email-address-field)
- [Enable Flash Checkout](#enable-flash-checkout)
- [Manage Fee Bearer Model](#manage-fee-bearer-model)
- [Enable International Payments](#enable-international-payments)
- [Manage Email Notifications](#manage-email-notifications)
- [Manage SMS Notifications](#manage-sms-notifications)
- [Manage WhatsApp Notifications](#manage-whatsapp-notifications)
- <a href="/docs/payments/payments/capture-settings/" target="_blank">Configure Payment Capture Settings</a>
- <a href="/docs/payments/refunds/refund-speed/" target="_blank">Change Default Refund Speed</a>

</show-if>


<show-if org="axis">

- [Change Checkout Theme](#change-checkout-theme)
- [Configure Email Address Field](#configure-email-address-field)
- [Enable Flash Checkout](#enable-flash-checkout)
- [Manage Fee Bearer Model](#manage-fee-bearer-model)
- [Enable International Payments](#enable-international-payments)
- [Manage Email Notifications](#manage-email-notifications)
- [Manage SMS Notifications](#manage-sms-notifications)
- [Manage WhatsApp Notifications](#manage-whatsapp-notifications)
- <a href="/docs/payments/payments/capture-settings/" target="_blank">Configure Payment Capture Settings</a>
- <a href="/docs/payments/refunds/refund-speed/" target="_blank">Change Default Refund Speed</a>


</show-if>


<show-if org="razorpay" country="MY">

- [Change Checkout Theme](#change-checkout-theme)
- [Manage Fee Bearer Model](#manage-fee-bearer-model)
- [Manage Email Notifications](#manage-email-notifications)
- [Manage SMS Notifications](#manage-sms-notifications)
- [Manage WhatsApp Notifications](#manage-whatsapp-notifications)
- <a href="/docs/payments/payments/capture-settings/" target="_blank">Configure Payment Capture Settings</a>
- <a href="/docs/payments/refunds/refund-speed/" target="_blank">Change Default Refund Speed</a>

</show-if>


# Change Checkout Theme

Following are the customizations you can do on the Checkout page:

## Change Color on Checkout Page

To change color on the Checkout page:

1. In the **Theme Color** field, enter the HEX code of your brand color. Alternatively, click on the color box and enter the RGB code.
2. Click **Save**.

## Upload Company Logo

Click **Choose File** to upload your company logo.

<callout info>

**Handy Tips**

* The logo file size should not exceed 1MB.
* Upload a square image of minimum dimensions 256x256 px.
</callout>

## Select Default Language

The customers can <a href='https://razorpay.com/docs/payment-gateway/web-integration/standard/local-lang/' target='_blank'>view the Checkout page in their preferred language</a>.

If the customer does not specify a language, the default language will be used on the checkout page. To select the default checkout language:

1. Use the drop-down list to view the language options.
2. Select the default language. For example, **English**.
3. Click **Save**.

<show-if org="razorpay" country="IN">

<img class="click-zoom" src="/docs/assets/images/dashboard-guide-settings-checkout-theme1.jpg" alt="customise checkout theme" width='800'/>


# Configure Email Address Field
By default, the email address field is hidden on checkout. You can choose to configure the email address field based on your requirement:
1. Log in to the <a href="https://dashboard.razorpay.com/#/app" target="_blank">Razorpay Dashboard</a>.
2. Navigate to **Account & Settings**
3. Click **Branding** under the **Checkout settings** section.
   <img src="/docs/assets/images/dashboard-checkout-settings.jpg" alt="Dashboard checkout settings for email" width="800"/>
4. In the **Collect email address from users on Checkout page** field, you can select:
   - **No (Default)**: Customers will not be shown this field on checkout.
   - **As an optional field**: Customers can either enter their email address or choose to skip it.
   - **As a mandatory field**: Customers have to enter their email address to proceed.
   <img src="/docs/assets/images/dashboard-emailess-checkout.jpg" alt="Email-less checkout configuration on dashboard" width="800"/>
5. Click **Save**.

</show-if>

<show-if org="axis">

# Configure Email Address Field
By default, the email address field is hidden on checkout. You can choose to configure the email address field based on your requirement:
1. Log in to the <a href="https://axis.razorpay.com/#/app" target="_blank">Axis Dashboard</a>.
2. Navigate to **Account & Settings**
3. Click **Branding** under the **Checkout settings** section.
4. In the **Collect email address from users on Checkout page** field, you can select:
   - **No (Default)**: Customers will not be shown this field on checkout.
   - **As an optional field**: Customers can either enter their email address or choose to skip it.
   - **As a mandatory field**: Customers have to enter their email address to proceed.
5. Click **Save**.

</show-if>

<show-if org="razorpay" country="IN">

# Enable Flash Checkout

## About Flash Checkout

Flash Checkout is the easiest way to allow your customers to securely save their credit and/or debit card details with Razorpay, thereby reducing transaction time.

Customers need to authenticate themselves only once on their mobile devices. Razorpay is PCI-DSS compliant. All the card information is securely saved on our servers.

After the one-time authentication, customers' saved cards are available to accept payments online via Razorpay. This allows for much simpler and faster transactions.

You can enable or disable flash checkout from the **Configuration** tab. Flash checkout is enabled by default. Click **Disable Flash Checkout** to disable it.

## Enable/Disable Flash Checkout

Watch this video to see how to enable or disable Flash Checkout:

<iframe width="560" style='max-width:100%' height="315" src="https://www.youtube.com/embed/Vm_8yjjmN3I" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Manage Saved Cards

Customers can manage their saved card details stored as tokens using our portal. 
- <a href="https://razorpay.com/flashcheckout/manage/" target="_blank">Manage Global Saved Cards</a> by following the on-screen instructions.
- <a href="/docs/payments/payment-methods/cards/features/manage/" target="_blank">Manage Local Saved Tokens</a>. 

</show-if>

<show-if org="axis">

# Enable Flash Checkout

## About Flash Checkout

Flash Checkout is the easiest way to allow your customers to securely save their credit and/or debit card details with Razorpay, thereby reducing transaction time.

Customers need to authenticate themselves only once on their mobile devices. Razorpay is PCI-DSS compliant. All the card information is securely saved on our servers.

After the one-time authentication, customers' saved cards are available to accept payments online via Razorpay. This allows for much simpler and faster transactions.

You can enable or disable flash checkout from the **Configuration** tab. Flash checkout is enabled by default. Click **Disable Flash Checkout** to disable it.

## Enable/Disable Flash Checkout

## Manage Saved Cards

Customers can manage their saved card details stored as tokens using our portal. 
- <a href="https://razorpay.com/flashcheckout/manage/" target="_blank">Manage Global Saved Cards</a> by following the on-screen instructions.
- <a href="/docs/payments/payment-methods/cards/features/manage/" target="_blank">Manage Local Saved Tokens</a>. 

</show-if>

# Manage Fee Bearer Model

For every payment done using Razorpay, we levy a nominal platform fee. You can choose to charge a Convenience Fee to your customers for the use of technology infrastructure. Convenience Fees are seamlessly added at Razorpay Checkout without disrupting the checkout experience for your customers. In case a refund is initiated, your customers receive the Convenience Fees along with the actual payment amount.

To manage fee bearer model:

<show-if org="razorpay" country="IN">

1. Log in to the <a href="https://dashboard.razorpay.com/#/app" target="_blank">Razorpay Dashboard</a>.
2. Navigate to **Account & Settings**.
3. Select the **Convenience Fee Model** option on the **Settings** → **Fee Bearer** section of the Razorpay Dashboard.
   <img src="/docs/assets/images/dashboard-guide-settings-fee-bearer-customer-fee-bearer.jpg" alt="Customer pays the fee" width="800"/>
   
</show-if>

<show-if org="razorpay" country="MY">

1. Log in to the <a href="https://dashboard.curlec.com/#/app" target="_blank">Curlec Dashboard</a>.
2. Navigate to **Account & Settings**.
3. Select the **Convenience Fee Model** option on the **Settings** → **Fee Bearer** section of the Curlec Dashboard.
   
</show-if>


<show-if org="axis">

1. Log in to the <a href="https://axis.razorpay.com/#/app" target="_blank">Axis Dashboard</a>.
2. Navigate to **Account & Settings**.
3. Select the **Convenience Fee Model** option on the **Settings** → **Fee Bearer** section of the Curlec Dashboard.

</show-if>



Know more about <a href="/docs/payments/dashboard/settings/configuration/convenience-fees" target="_blank">this feature</a>.

<show-if org="razorpay" country="IN">

# Enable International Payments

By default, you can accept payments in various <a href="/docs/international-payments/#supported-currencies" target="_blank">international currencies supported by Razorpay</a>.

If you do not want to accept payments in currencies apart from INR (₹), you can turn it off using the toggle switch available here.

Watch this video to see how to enable international payments.

<iframe width="560" style='max-width:100%' height="315" src="https://www.youtube.com/embed/lPvasqEJqK8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Refer to our <a href="https://razorpay-ind.freshdesk.com/support/solutions/folders/82000427888" target="_blank">International Payments Knowledgebase</a> for some FAQs.

</show-if>


<show-if org="axis">

# Enable International Payments

By default, you can accept payments in various <a href="/docs/international-payments/#supported-currencies" target="_blank">international currencies supported by Razorpay</a>.

If you do not want to accept payments in currencies apart from INR (₹), you can turn it off using the toggle switch available here.

Refer to our <a href="https://razorpay-ind.freshdesk.com/support/solutions/folders/82000427888" target="_blank">International Payments Knowledgebase</a> for some FAQs.

</show-if>


# Manage Notifications

## Manage Email Notifications

You can configure the email addresses to receive email notifications like payments received, daily payment reports and webhooks. You will also receive an email notification for both successful and failed settlements.

<callout info>
**Handy Tips**

Settlement emails will be sent to the email addresses provided on the Dashboard. Know more about <a href="/docs/payment-gateway/settlements/" target="_blank">Settlements</a>.
</callout>

To enable email notifications:


1. Log in to the Dashboard.
2. On the left navigation, click **Accounts & Settings**.
3. Navigate to **Notification settings → Email**.
4. Enter email addresses under **Email Notifications**. If you want to enter multiple email addresses, separate them by a comma.


<show-if org="razorpay" country="IN">

<img src="/docs/assets/images/manage-email-notifications.jpg" alt="Manage Email Notifications" width="800"/>

</show-if>

## Manage SMS Notifications

You can enable **SMS Notifications** to receive SMS notifications for successful and failed settlements.

To enable SMS notifications:


1. Log in to the Dashboard.
2. Click **Accounts & Settings** and go to **Notification settings → SMS**.
3. Enable **SMS Notifications**.

<show-if org="razorpay" country="IN">

<img src="/docs/assets/images/manage-sms-notifications.jpg" alt="Manage SMS Notifications" width="800"/>

</show-if>

Once enabled, you will start receiving notifications on the registered phone number.

By default, this feature is set to **Enabled**. You can disable it using the toggle button.

<show-if org="razorpay" country="IN">

<img src="/docs/assets/images/manage-sms-notifications-disable-new.jpg" alt="Manage SMS Notifications" width="800"/>

</show-if>

## Manage WhatsApp Notifications

You can receive WhatsApp notifications regarding settlements, account configuration changes and more on your registered contact number.

<callout info>
**Handy Tips**

This feature is available only to the owner user role.
</callout>

You can enable this feature during the sign up process or later from the Razorpay Dashboard.

To enable WhatsApp notifications:


1. Log in to the Dashboard.
2. Click **Accounts & Settings** and go to **Notification settings → WhatsApp**.
3. Enable **WhatsApp Notifications**.

<show-if org="razorpay" country="IN">

<img src="/docs/assets/images/manage-whatsApp-notifications.jpg" alt="Manage WhatsApp Notifications" width="800"/>

</show-if>

Once enabled, you will start receiving notifications on the registered number.

You can disable the WhatsApp notifications at any time on the <brand-name/> Dashboard.

<show-if org="razorpay" country="IN">

<img src="/docs/assets/images/manage-whatsApp-notifications-disable.jpg" alt="Manage WhatsApp Notifications" width="800"/>

</show-if>

