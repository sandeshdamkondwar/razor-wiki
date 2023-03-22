---
title: Dashboard | Payment Methods
razorpay-MY-title: Dashboard | Payment Methods
heading: Payment Methods
razorpay-MY-heading: Payment Methods
desc: Enable and disable different Payment Methods from the Razorpay Dashboard. Learn about Coverage, Pricing, and Responding to Action Required status.
razorpay-MY-desc: View Payment Methods from the Curlec Dashboard. Learn about Coverage, Pricing, and Responding to Action Required status.
---

<show-if org="razorpay" country="IN">

You can view the payment methods enabled for your Razorpay account from the **Account & Settings → Payment Methods** tab. Also, you can raise requests for additional payment methods. The requests initiated from this panel are raised with our partner banks and the onboarding process for the payment method is started.

<callout info>
**Handy Tips**

- This feature is available only on the Live mode of the Razorpay Dashboard.
- Users with the following User Roles can configure the payment methods:
    - Owner
    - Admin
    - Manager
</callout>

</show-if>

<show-if org="razorpay" country="MY">

You can view the payment methods enabled for your Curlec account from the **Account & Settings → Payment Methods** tab.

<callout info>
**Handy Tips**

- This feature is available only on the Live mode of the Curlec Dashboard.
- Users with the following User Roles can configure the payment methods:
    - Owner
    - Admin
    - Manager
</callout>

</show-if>

<show-if org="razorpay" country="IN">

# Enable Payment Methods

Activation of each of the payment methods involves onboarding with our partner banks. The average activation time is currently 10 working days, although this can vary across methods and banks.

## States

Under the **Payment Methods** tab, you can view the list of payment methods and their status.

<img class="click-zoom" src="/docs/assets/images/dashboard-guide-payment-methods-setting_1.jpg" alt="Payment methods tab on the Razorpay Dashboard" width="800"/>

Some of the payment methods are enabled by default, while you need to raise a request for some. Mentioned below are the various statuses your request can go through.

<table>
Status | Description
---
**Under Review** | Our team is validating the information provided.
---
**Updated** | The provided information is verified successfully.
---
**Requested** | A request has been raised, but no action has been taken yet.
---
**Cancelled** | A request was initially raised but was later cancelled by you or your team member.
---
**Pending** | The request has been taken up for onboarding by our partner banks.
---
**Action Required** | In some cases, we may not be able to fulfill a request as our banking partners seek certain clarifications. For example, there may be some missing information in the activation form. In such cases, the request will be placed in the `Action Required` state, along with a comment indicating the actions required from your end. You can [respond to the Action Required](#respond-to-action-required) status.
---
**Rejected** | The request is rejected for your account. This generally happens due to category restrictions. See the Comments for more information.
---
**Re-initiated** | The previous request in the `Action Required` state has now been re-initiated after the action is complete.
---
**Activated** | This indicates that the method is now live and available on standard checkout.
</table>

## Request for Payment Methods

Watch this video to see how to raise a request for a payment method. <br/><br/>
<iframe width="560" height="315" src="https://www.youtube.com/embed/L7VXx1mRJBs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

To raise a request for a payment method:
1. On the Razorpay Dashboard, select **Accounts & Settings** on the left navigation.  
2. Click on the payment method you want to request under **Payment Methods** tab, for example Cards.
    <img class="click-zoom" src="/docs/assets/images/pm-cards_1.jpg" alt="Select payment methods cards on the Razorpay Dashboard" width="700"/>
3. Click the dropdown on the **Additional details required** tab and click **Add now** to update the business website or GSTIN details.
    <img class="click-zoom" src="/docs/assets/images/pm-add-info_1.jpg" alt="Payment methods - cards - add additional details" width="700"/>

    <callout warn>
    **Watch Out!**

    The **Additional details required** tab must be updated to request any payment method.
    </callout>

4. Fill in the business website/app details and click **Proceed to update website/app**. Know more about <a href="/docs/payments/dashboard/my-account/profile/#add-or-update-websiteapp-details" target="_blank">how to add website details</a>.
    <img class="click-zoom" src="/docs/assets/images/pm-add-website-info.jpg" alt="Payment methods add website info" width="700"/>
5. Fill in the GSTIN details and click **Submit**. Know more about <a href="/docs/payments/dashboard/my-account/profile/#add-or-update-gst-details" target="_blank">how to add GSTIN details</a>.
    <img class="click-zoom" src="/docs/assets/images/pm-add-gstin-info.jpg" alt="Payment methods add gstin info" width="500"/>

    <callout info>
    **Handy Tips**

    The **Additional details** are requested by our banking partners and are specific to a specific payment method.
    </callout>

6. Once you submit all the required information, the status of the information provided changes to **Under Review**.
    <img class="click-zoom" src="/docs/assets/images/pm-review.jpg" alt="Payment methods under review" width="700"/>

8. Once the required information is reviewed and updated, click **Request**.
    <img class="click-zoom" src="/docs/assets/images/pm-status-request.jpg" alt="Payment methods status request" width="700"/>
9. Fill in the required details and click **Next**.
    <img class="click-zoom" src="/docs/assets/images/pm-save-details_1.jpg" alt="Payment methods additional details required" width="600"/>
10. Click **Submit Request**.
    <img class="click-zoom" src="/docs/assets/images/pm-submit-request.jpg" alt="Payment methods submit request" width="600"/>
11. The status of the payment method changes to **Requested**.
    <img class="click-zoom" src="/docs/assets/images/status-requested.jpg" alt="Payment methods status requested" width="600"/>

# Disable Payment Methods

Raise a request with our <a href="https://razorpay.com/support/" target="_blank">Support team</a> to disable any Payment Method.

# Respond to Action Required
You can respond to any discrepancies or clarifications raised for payment method requests with comments, attachments or both.<br/>
Our Banking Ops team validates your payment method request. If they find any discrepancies or need further clarification regarding the website or documents, we change the request status from **Pending** to **Action Required**. You can provide these details from the Dashboard.<br/>
To respond to the discrepancies or clarifications requested:
1. On the <a href="https://dashboard.razorpay.com/" target="_blank">Razorpay Dashboard</a>, select the **Account & Settings → Payment Methods** tab. Click **Payment Methods**.
2. Look for the Payment Method you asked for and click on **Update Request Form**.
    <img class="click-zoom" src="/docs/assets/images/pg-2-way-action.jpg" alt="Payment methods update request form" width="800"/>
3. Fill in the clarifications asked.
4. Fill in the required details or add attachments if requested and click **Submit Form**.
    <img class="click-zoom" src="/docs/assets/images/pg-2-way-submit-form.jpg" alt="Clarifications needed for payment methods request form" width="800"/>
5. The status of your request changes from **Action Required** to **Reinitiated**.
    <img class="click-zoom" src="/docs/assets/images/pm-requested.jpg" alt="Payment methods request status reinitiated" width="800"/>


Razorpay re-reviews requests and responds within 7 days.

</show-if>

# Coverage and Pricing

<show-if org="razorpay" country="IN">

## Coverage
The **Payment Methods** tab shows most payment instruments that we can freely enable for your account. We keep updating this page to allow us to enable more instruments. If you have questions about specific instruments, feel free to reach out to our <a href="https://razorpay.com/support/#request" target="_blank">Support team</a>.

## Pricing
All methods requested via the Payment Methods tab will be enabled for your account using <a href="https://razorpay.com/pricing/" target="_blank">Standard Pricing</a>, or the default pricing configured for the payment method for your Razorpay account.

</show-if>

<show-if org="razorpay" country="MY">

## Coverage
The **Payment Methods** tab shows most payment instruments that we can freely enable for your account. We keep updating this page to allow us to enable more instruments. If you have questions about specific instruments, feel free to reach out to our <a href="success@curlec.com">Support team</a>.

## Pricing
All methods requested via the Payment Methods tab will be enabled for your account using Standard Pricing, or the default pricing configured for the payment method for your Curlec account.

</show-if>