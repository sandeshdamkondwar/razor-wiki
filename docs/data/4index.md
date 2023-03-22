---
title: API Keys
desc: Generate and regenerate Test and Live API Keys using the Razorpay Dashboard.
---

API key is a combination of the `key_id` and `key_secret` and is required to make any API request to Razorpay. You also have to implement the API key in your code as part of your integration process.

# Generate API Keys

@include generate_api-key

Once generated, you will be able to see the Key Id, the date the key was created and the expiry date for the API Key on screen.

<show-if org="razorpay" country="IN">

<img src="/docs/assets/images/settings-4.jpg" alt="Live mode API keys generated on the Razorpay dashboard" width="800"/>

</show-if>

# Regenerate API Keys

You also have the option to regenerate the key if required.

<callout info>
**Two-Factor Authentication**

To regenerate API keys, you must validate your identity via OTP sent to your registered mobile number. However, this step is skipped if you already performed OTP validation while logging in to the Dashboard.

If you have not set up two-factor authentication, you will be prompted to verify your mobile number before re-generating keys.
</callout>

<show-if org="razorpay" country="IN">

To regenerate API key:

1. Log in to the <a href="https://dashboard.razorpay.com/#/access/signin" target="_blank">Razorpay Dashboard</a>.
1. Select the mode for which you want to generate the API key from the menu ribbon.
1. Navigate to **Account & Settings** → **API Keys** (under Website and app settings) → Generate Key to generate key for the selected mode.
1. Click **Regenerate Key**.

This gives you the option to deactivate the old key immediately or in 24 hours.

Watch the short animation below for more information.

<img src="/docs/assets/images/dashboard-guide-regenerate-api-key.gif" alt="Regenerate API keys on the Razorpay dashboard" width="800"/>

</show-if>

<show-if org="razorpay" country="MY">

To regenerate API key:

1. Log in to the <a href="https://dashboard.curlec.com/#/access/signin" target="_blank">Curlec Dashboard</a>.
1. Select the mode for which you want to generate the API key from the menu ribbon.
1. Navigate to **Account & Settings** → **API Keys** (under Website and app settings) → Generate Key to generate key for the selected mode.
1. Click **Regenerate Key**.

This gives you the option to de-activate the old key immediately or in 24 hours.

</show-if>


<show-if org="axis">

To regenerate API keys:

1. Log in to the <a href="https://axis.razorpay.com/" target="_blank">Dashboard</a>.
1. Select the mode for which you want to generate the API key from the menu ribbon.
1. Navigate to **Account & Settings** → **API Keys**.
1. Click **Regenerate Key**.

This gives you the option to deactivate the old key immediately or in 24 hours.


</show-if>

# Related Information

- <a href="/docs/api/best-practices" target="_blank">API Best Practices</a>
- <a href="/docs/api/glossary/" target="_blank">API Glossary</a>
- <a href="/docs/payments/dashboard/faqs#2-i-cannot-generate-live-mode-api-keys" target="_blank">API Keys FAQ</a>
- <a href="/docs/payments/dashboard/settings/configuration" target="_blank">Dashboard Configuration</a>

