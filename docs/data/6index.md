---
title: Profile
razorpay-MY-title: Profile
desc: View your account details, add GST number, and request a change to your settlement account under the Profile tab on the Razorpay Dashboard.
razorpay-MY-desc: View your account details, and request a change to your settlement account under the Profile tab on the Curlec Dashboard.
---

<show-if org="razorpay" country="IN">

You can view your account details under the **Profile** tab, such as Merchant Name, Email, GST details, Business Name and Type, Settlement Account details, Razorpay Account Registration and Activation dates and KYC Form Status.

From this tab, you can do the following:
- [Enable 2-step verification at the account level](#2-step-verification-account-level).
- [Add or Update GST details](#add-or-update-gst-details).
- [Request a change to your settlement (bank) account](#change-bank-account-details).
- [Update login email](#update-login-email).
- [Add support details](#add-support-details).
- [Add or update website/app details](#add-or-update-website-or-app-details).
- [Add or update additional website details](#add-or-update-additional-website-details)
- [Update limit per domestic transaction](#update-limit-per-domestic-transaction).
- [Update limit per international transaction](#update-limit-per-international-transaction).
- [Update brand name](#update-brand-name).
- [Update Importer Exporter Code (IEC)](#update-importer-exporter-code-iec)
- You can also perform other actions such as changing your account password, display name and contact number.

</show-if>

<show-if org="axis">

You can view your account details under the **Profile** tab, such as Merchant Name, Email, GST details, Business Name and Type, Settlement Account details, Razorpay Account Registration and Activation dates and KYC Form Status.

From this tab, you can do the following:
- [Enable 2-step verification at the account level](#2-step-verification-account-level).
- [Add or Update GST details](#add-or-update-gst-details).
- [Request a change to your settlement (bank) account](#change-bank-account-details).
- [Update login email](#update-login-email).
- [Add support details](#add-support-details).
- [Add or update website/app details](#add-or-update-website-or-app-details).
- [Add or update additional website details](#add-or-update-additional-website-details)
- [Update limit per domestic transaction](#update-limit-per-domestic-transaction).
- [Update limit per international transaction](#update-limit-per-international-transaction).
- [Update brand name](#update-brand-name).
- [Update Importer Exporter Code (IEC)](#update-importer-exporter-code-iec)
- You can also perform other actions such as changing your account password, display name and contact number.

</show-if>

<show-if org="razorpay" country="MY">

You can view your account details under the **Profile** tab, such as Merchant Name, Email, Business Name and Type, Settlement Account details, Curlec Account Registration and Activation dates and KYC Form Status.

From this tab, you can do the following:
- [Enable 2-step verification at the account level](#2-step-verification-account-level).
- [Request a change to your settlement (bank) account](#change-bank-account-details).
- [Update login email](#update-login-email).
- [Add support details](#add-support-details).
- [Add or update website/app details](#add-or-update-website-or-app-details).
- [Add or update additional website details](#add-or-update-additional-website-details)
- [Update limit per domestic transaction](#update-limit-per-domestic-transaction).
- [Update limit per international transaction](#update-limit-per-international-transaction).
- [Update brand name](#update-brand-name).
- You can also perform other actions such as changing your account password, display name and contact number.

</show-if>

# 2-Step Verification (Account Level)

<brand-name/> provides enhanced security and protection through 2-step verification for all <brand-name/> Dashboard users.

## What is 2-Step Account Verification (Two-factor Authentication, 2FA)

To log in to the <brand-name/> Dashboard, users enter their email address and password. If the 2-step verification is enabled on an account, the user should enter a One Time Password (OTP) after the email id and password is provided. The OTP is sent to the user's registered mobile number.

You can set this additional level of security to ensure that only the intended user has access to your <brand-name/> Dashboard, thus preventing malicious attacks or misuse of your sensitive business data.

<callout info>
**Team 2-Step Verification**

To enable 2-step verification for your entire team, see <a href="/docs/payment-gateway/dashboard-guide/manage-team/#2-step-verification" target="_blank">Manage Team</a>.
</callout>

<show-if org="razorpay" country="IN">

Watch this video to see how to enable 2FA for your account. <br/><br/>
<iframe width="560" style='max-width:100%' height="315" src="https://www.youtube.com/embed/-wuM_3QpmbM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

To enable 2-step verification for your account:
1. Log in to the <a href="https://dashboard.razorpay.com/#/app" target="_blank">Razorpay Dashboard</a>.
1. Click **Account & Settings** in the left navigation.
1. Enable the **2-Step Verification** option under **Your Profile**.
1. Enter the OTP sent to your registered mobile number.
1. Enter your account password and confirm.

You have now set a 2FA for your account.

</show-if>

<show-if org="axis">

To enable 2-step verification for your account:
1. Log in to the Axis Dashboard.
1. Click **Account & Settings** in the left navigation.
1. Enable the **2-Step Verification** option under **Your Profile**.
1. Enter the OTP sent to your registered mobile number.
1. Enter your account password and confirm.

You have now set a 2FA for your account.

</show-if>

<show-if org="razorpay" country="MY">

To enable 2-step verification for your account:
1. Log in to the <a href="https://dashboard.curlec.com/?screen=sign_in" target="_blank">Curlec Dashboard</a>.
2. Navigate to **Account & Settings** → **Profile**.
3. Enable the **2-Step Verification** option.
4. Enter the OTP sent to your registered mobile number.
5. Enter your account password and confirm.

You have now set a 2FA for your account.

</show-if>

## FAQs

#### 1. What to do if a user account is locked?
If a user enters the wrong OTP 9 times, the user account gets locked for security reasons. In such scenarios, the user should contact their respective account owner. The account owner can unlock the user's account. Know more about various <a href="/docs/payments/dashboard/my-account/manage-team/" target="_blank">Team Roles</a>.

#### 2. What to do if a user loses the mobile device?
If a user loses the mobile device, the user should reach out to the respective account owner. The account owner can **Invalidate 2FA** for the user, which resets 2FA for the user. The user needs to enter the mobile number the next time he/she logs into the <brand-name/> Dashboard.

<show-if org="razorpay" country="IN">
Watch this video to see how the account owner can reset 2FA for a team member.<br/><br/>
<iframe width="560" style='max-width:100%' height="315" src="https://www.youtube.com/embed/6PWz3RMEdoo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</show-if>

<show-if org="razorpay" country="IN">

#### 3. What to do if the account owner's account is locked?
If you are an account owner and enter the wrong OTP 9 times, your account gets locked for security reasons. In such scenarios, contact our <a href="https://razorpay.com/support/#request" target="_blank">Support Team</a> to **Reset 2FA** for your account.

</show-if>

<show-if org="razorpay" country="MY">

#### 3. What to do if the account owner's account is locked?
If you are an account owner and enter the wrong OTP 9 times, your account gets locked for security reasons. In such scenarios, contact our <a href="success@curlec.com">Support Team</a> to **Reset 2FA** for your account.

</show-if>

#### 4. What to do if the account owner loses the mobile device?

<show-if org="razorpay" country="IN">
If you are an account owner and have lost your mobile device, contact our <a href="https://razorpay.com/support/#request" target="_blank">Support Team</a> to **Reset 2FA** for your account.
</show-if>

<show-if org="razorpay" country="MY">
If you are an account owner and have lost your mobile device, contact our <a href="success@curlec.com">Support Team</a> to **Reset 2FA** for your account.
</show-if>

<show-if org="razorpay" country="IN">

# Add or Update GST details

You can add or update your GST details from the Razorpay Dashboard.

<callout warn>
**Watch Out!**

Your account details like name, business name, and registered address will change as per the updated GST details.
</callout>

<callout info>
**Handy Tips**

- This feature is available only for registered Razorpay users.
- Only users with 'Owner' or 'Admin' roles can add or update the GST details.
</callout>

To add or update GST details:
1. Log in to your <a href="https://dashboard.razorpay.com/#/access/signin" target="_blank">Razorpay Dashboard</a>.
2. Click **Account & Settings** in the left navigation.
3. Click **GST details** under **Business Settings**.
    - To add your GST details, click **Add GST details**.
    <img class="click-zoom" width="700" src="/docs/assets/images/dashboard-guide-profile-add-gst-details.jpg" alt="Add GST details on the Razorpay Dashboard"/>
    - To update your GST details, click **Update GST details**.
4. In the **Add GST details** pop-up page:
    - Enter the GSTIN. This will appear on the invoices sent by Razorpay.
    - Upload a copy of the GSTIN Certificate and click **Submit**.
    <img class="click-zoom" width="300" src="/docs/assets/images/dashboard-guide-profile-add-gst.jpg" alt="Submit GST details on Razorpay Dashboard"/>


After you provide the details, our team will review the request. During the verification process, we may reach out to you for clarifications.

## FAQs

#### 1. After updating the GST details, will the older invoices still be associated with my old GST value?
Yes, invoices downloaded before updating the GST details will have the older value of GSTIN associated with them.

</show-if>

# Change Bank Account Details

You can request a change to your settlement (bank) account linked to your account. After you provide the necessary details and documents, we will verify the account and update the information. We will contact you if further clarifications are required.

<show-if org="razorpay" country="IN">

<callout info>
**Handy Tips**

You need to send us a copy of the new account's account statement that you want to link to your <brand-name/> account. The account statement should include details such as account number, IFSC and beneficiary. It should contain transaction details for the last three months or since the account was opened, whichever is later.
</callout>

Watch this video to see how you can change your settlement account details from the Razorpay Dashboard. <br/><br/>
<iframe width="560" style='max-width:100%' height="315" src="https://www.youtube.com/embed/vUVb6FdPMnA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

To request a bank account change:
1. Log in to your <a href="https://dashboard.razorpay.com/#/access/signin" target="_blank">Razorpay Dashboard</a>.
1. Click **Account & Settings** in the left navigation.
1. Click **Bank account details** under **Bank accounts and settlements** section and click **Change bank account**.
1. Enter the OTP sent to your registered mobile device on the **2-Step Verification** pop-up page.
1. Enter the details of the new bank account you want to link with your Razorpay account. The new bank account will be your new settlement account.
1. Upload a copy of your account statement and click **Save**.

</show-if>


<show-if org="axis">

<callout info>
**Handy Tips**

You need to send us a copy of the new account's account statement that you want to link to your <brand-name/> account. The account statement should include details such as account number, IFSC and beneficiary. It should contain transaction details for the last three months or since the account was opened, whichever is later.
</callout>


To request a bank account change:
1. Log in to the Dashboard.
1. Click **Account & Settings** in the left navigation.
1. Click **Bank account details** under **Bank accounts and settlements** section and click **Change bank account**.
1. Enter the OTP sent to your registered mobile device on the **2-Step Verification** pop-up page.
1. Enter the details of the new bank account you want to link with your Razorpay account. The new bank account will be your new settlement account.
1. Upload a copy of your account statement and click **Save**.

</show-if>

<show-if org="razorpay" country="MY">

<callout info>
**Handy Tips**

You need to send us a copy of the new account's account statement that you want to link to your Curlec account. It should contain transaction details for the last three months or since the account was opened, whichever is later.
</callout>

To request a bank account change:
1. Log in to your <a href="https://dashboard.curlec.com/?screen=sign_in" target="_blank">Curlec Dashboard</a>.
1. Navigate to **Account & Settings** and click **Profile**.
1. Scroll to the **Bank Account** section and click **Request Change**.
1. Enter the OTP sent to your registered mobile device on the **2-Step Verification** pop-up page.
1. Enter the details of the new bank account you want to link with your Curlec account. The new bank account will be your new settlement account.
1. Upload a copy of your account statement and click **Save**.

</show-if>

<callout info>
**Handy Tips**

<brand-name/> sends you email notifications for the following:
- When you initiate a request for updating the settlement bank account details.
- When the bank account details are successfully updated.
</callout>

<callout info>
**Handy Tips**

We may reach out to you for clarifications via email, WhatsApp, SMS, and <brand-name/> Dashboard during the verification process.
Navigate to **Account & Settings** → **Profile** and submit the necessary information in the appropriate section. Our team will go through the information you provide and help you resolve the issue.
</callout>

# Update Login Email 

<show-if org="razorpay" country="IN">

You can update the Razorpay login email from the Razorpay Dashboard. You can:
- [Update your own email id](#update-your-email). <br/>
    Replace your current email id with another email. For example, if you earlier had signed up with the email id `info@acmecorp.in`, you can now update it as `gaurav.kumar@acmecorp.in`.
- [Add a team member's email id](#add-a-team-members-email). <br/>
    - You can add another team member's email id. You will need to change the user role of the team member to `owner`. For example, you can provide your manager's email id and upgrade them to the `owner` role.
    - You can add the email id of a Razorpay user who is not a member of your team. For example, Gauri Kumari is the manager of a Razorpay account, ABC Co. You want to add her as the `owner` of your Razorpay account, Acme Corp. Once you update her email address on the Dashboard, Gauri Kumari will become the `owner` of the Acme Corp account. However, she will still be the manager of the ABC Co Razorpay account.

</show-if>

<show-if org="axis">

You can update the Razorpay login email from the Razorpay Dashboard. You can:
- [Update your email id](#update-your-email). <br/>
    Replace your current email id with another email. For example, if you earlier had signed up with the email id `info@acmecorp.in`, you can now update it as `gaurav.kumar@acmecorp.in`.
- [Add a team member's email id](#add-a-team-members-email). <br/>
    - You can add another team member's email id. You will need to change the user role of the team member to `owner`. For example, you can provide your manager's email id and upgrade them to the `owner` role.
    - You can add the email id of a Razorpay user who is not a member of your team. For example, Gauri Kumari is the manager of a Razorpay account, ABC Co. You want to add her as the `owner` of your Razorpay account, Acme Corp. Once you update her email address on the Dashboard, Gauri Kumari will become the `owner` of the Acme Corp account. However, she will still be the manager of the ABC Co Razorpay account.

</show-if>

<show-if org="razorpay" country="MY">

You can update the Curlec login email from the Curlec Dashboard. You can:
- [Update your own email id](#update-your-email). <br/>
    Replace your current email id with another email. For example, if you earlier had signed up with the email id `info@acmecorp.in`, you can now update it as `siti.aisyah@acmecorp.in`.
- [Add a team member's email id](#add-a-team-members-email). <br/>
    - You can add another team member's email id. You will need to change the user role of the team member to `owner`. For example, you can provide your manager's email id and upgrade them to the `owner` role.
    - You can add the email id of a Cuelec user who is not a member of your team. For example, Nur Aisyah is the manager of a Curlec account, ABC Co. You want to add her as the `owner` of your Curlec account, Acme Corp. Once you update her email address on the Dashboard, Nur Aisyah will become the `owner` of the Acme Corp account. However, she will still be the manager of the ABC Co Curlec account.

</show-if>

<callout>
**Handy Tips**

If you add a non-<brand-name/> user's email id, they will have to sign up for a <brand-name/> account.
</callout>

## Update Your Email
As an account owner, you can update your <brand-name/> login email from the <brand-name/> Dashboard. 

To update login email:

<show-if org="razorpay" country="IN">

1. Log in to the <a href="https://dashboard.razorpay.com/#/access/signin" target="_blank">Razorpay Dashboard</a>.
1. Click **Account & Settings** in the left navigation.
1. Click **Email** under **Notification settings** section and click the edit icon.
    <img class="click-zoom" src="/docs/assets/images/dashboard-guide-profile-update-email.jpg" alt="Update email id from Razorpay Dashboard profile"/>
1. Complete the 2-factor authentication process.
1. On the pop-up page, enter the new email id. Re-enter the email id. Select the check box if you want Razorpay to send all communication details to this email id.
    <img class="click-zoom" width="300" src="/docs/assets/images/dashboard-guide-profile-email-id-repeat.jpg" alt="enter new email id"/>
1. A verification email is sent to your new email id. Open the email and complete the verification process.
    <img class="click-zoom" width="300" src="/docs/assets/images/dashboard-guide-profile-verification.jpg" alt="Complete verification process from your email id"/> <br/> 
    <br/>
    <img class="click-zoom" width="800" src="/docs/assets/images/dashboard-guide-profile-verify-email.jpg" alt="Verification email from Razorpay"/>

The email id has been updated.
<img class="click-zoom" width="300" src="/docs/assets/images/dashboard-guide-profile-updated-email.jpg" alt="Email updated successfully on dashboard profile"/>

</show-if>

<show-if org="axis">

1. Log in to the <a href="https://axis.razorpay.com/" target="_blank">Dashboard</a>.
2. Navigate to **Account & Settings** and click **Profile**.
3. Scroll to the **Login Email** field, click the edit icon. <br/>
4. Complete the 2-factor authentication process.
5. On the pop-up page, enter the new email id. Select the check box if you want Razorpay to send all communication details to this email id.
6. A verification email is sent to your email id. Open the email and complete the verification process.

Your email id has been updated.
</show-if>

<show-if org="razorpay" country="MY">

1. Log in to the <a href="https://dashboard.curlec.com/?screen=sign_in" target="_blank">Curlec Dashboard</a>.
2. Navigate to **Account & Settings** and click **Profile**.
3. Scroll to the **Login Email** field, click the edit icon.
4. Complete the 2-factor authentication process.
5. On the pop-up page, enter the new email id. Re-enter the email id. Select the check box if you want Curlec to send all communication details to this email id.
6. A verification email is sent to your new email id. Open the email and complete the verification process.

The email id has been updated.

</show-if>

## Add a Team Member's Email

You can make another member from your team the <brand-name/> account owner and add their email address as the login email id.

Follow these steps:

<show-if org="razorpay" country="IN">

1. Log in to the <a href="https://dashboard.razorpay.com/#/access/signin" target="_blank">Razorpay Dashboard</a>.
2. Navigate to **Account & Settings** and click **Manage Team**.
3. On the **Manage Team** page, click **Change** next to the **Owner**.
4. Select the team member whose role is to be upgraded and click **Change Owner**.
5. The email id has been updated.
    <img class="click-zoom" width="300" src="/docs/assets/images/dashboard-guide-profile-user-role-changed.jpg" alt="user role and email id changed"/>
</show-if>

<show-if org="axis">

1. Log in to the <a href="https://axis.razorpay.com/" target="_blank">Dashboard</a>.
2. Navigate to **Account & Settings** and click **Manage Team**.
3. In the **Manage Team** page, click **Change** next to the **Owner**.
4. Select the team member whose role is to be upgraded and click **Change Owner**.
5. The email id has been updated.

</show-if>

<show-if org="razorpay" country="MY">

1. Log in to the <a href="https://dashboard.curlec.com/?screen=sign_in" target="_blank">Curlec Dashboard</a>.
2. Navigate to **Account & Settings** and click **Manage Team**.
3. On the **Manage Team** page, click **Change** next to the **Owner**.
4. Select the team member whose role is to be upgraded and click **Change Owner**.
5. The email id has been updated.

</show-if>

# Add Support Details

You can add your support details to the transaction emails sent to your customers. This will help your customers know how to reach you for any queries.

<show-if org="razorpay" country="IN">

Watch this video to see how to add support details. <br/><br/>
<iframe width="560" style='max-width:100%' height="315" src="https://www.youtube.com//embed/nsUR-FRQewk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

To add support details:
1. Log in to the <a href="https://dashboard.razorpay.com/#/access/signin" target="_blank">Razorpay Dashboard</a>.
2. Click **Account & Settings** in the left navigation.
1. Click **Customer support details** under **Business settings** section and click the edit icon.
3. Click **Add Details** and on the pop-up page, add the following details:
    - Support Phone number
    - Support Email id (This is a mandatory field)
    - Support URL (Your website's support page)
5. Click **Submit**.

</show-if>

<show-if org="axis">

To add support details:
1. Log in to the Dashboard.
1. Click **Account & Settings** in the left navigation.
1. Click **Customer support details** under the **Business settings** section and click the edit icon.
1. Click **Add Details** and on the pop-up page, add the following details:
    - Support Phone number
    - Support Email id (This is a mandatory field)
    - Support URL (Your website's support page)
1. Click **Submit**.

</show-if>

<show-if org="razorpay" country="MY">

To add support details:
1. Log in to the <a href="https://dashboard.curlec.com/?screen=sign_in" target="_blank">Curlec Dashboard</a>.
2. Navigate to **Account & Settings** and click **Profile**.
3. Scroll to the **Support Details** section and click **Add Details**.
4. On the pop-up page, add the following details:
    1. Support Phone number
    2. Support Email id (This is a mandatory field)
    3. Support URL (Your website's support page) 
5. Click **Submit**.

</show-if>

# Add or Update Website or App Details

You must provide your live website or mobile app details during account activation. Without these details, you will not be able to access live mode API keys and hence cannot accept payments from your website or app. However, you can still accept payments from customers using Invoices and Payment Links generated via the Dashboard.

<callout info>
**Handy Tips**

Payments are enabled on the above-mentioned website or mobile app only after KYC approval.
</callout>

## Add Website/Mobile App Details

<show-if org="razorpay" country="IN">

Watch this video to see how to add website/mobile app details. <br/><br/>
<iframe width="560" style='max-width:100%' height="315" src="https://www.youtube.com/embed/wHRRNvGWq3A" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

To add your website or mobile app details:
1. Log in to the <a href="https://dashboard.razorpay.com/#/app" target="_blank">Razorpay Dashboard</a>.
2. Click **Account & Settings** in the left navigation.
1. Click **Business website detail** under **Website and app settings** section.
3. Click **Fill Activation Form**.
4. In the form, for the Website/App URL field, select Website/App.
5. Provide the website details and click **Save & Next**. <br/>

</show-if>

<show-if org="axis">

To add your website or mobile app details:
1. Log in to the Dashboard.
2. Click **Account & Settings** in the left navigation.
1. Click **Business website detail** under the **Website and app settings** section.
3. Click **Fill Activation Form**.
4. In the form, for the Website/App URL field, select Website/App.
5. Provide the website details and click **Save & Next**. <br/>

</show-if>

<show-if org="razorpay" country="MY">

To add your website or mobile app details:
1. Log in to the <a href="https://dashboard.curlec.com/?screen=sign_in" target="_blank">Curlec Dashboard</a>.
2. Navigate to **Account & Settings** → **Profile**.
3. Click **Fill Activation Form**.
4. In the form, for the Website/App URL field, select Website/App.
5. Provide the website details and click **Save & Next**.

</show-if>

## Update Website/Mobile App Details

<show-if org="razorpay" country="IN">

To update website or mobile app details:
1. Log in to the <a href="https://dashboard.razorpay.com/#/app" target="_blank">Razorpay Dashboard</a>.
2. Click **Account & Settings** in the left navigation.
1. Click **Business website detail** under **Website and app settings** section.
3. Click the edit icon next to the **Business Website/App details** field.
4. In the pop-up page that is displayed, click **Proceed to update website/app**.
5. Provide the website or app details:
    - Follow these steps if you own a website:
        1. Select **Website**.
        2. Enter the **Website URL**. 
        3. Provide the links for these pages: **About us**, **Contact us**, **Pricing details**, **Terms and conditions**, **Privacy policy** and **Refunds policy**. 
        4. Provide your website's **Test Account credentials**. If the customer does not need to Log in to your website, select **My website doesn’t require log in to transact**.
        5. Click **Submit website for review**.
             <img class="click-zoom" src="/docs/assets/images/dashboard-guide-myaccount-profile-update-website-url.jpg" alt="Enter Website URL"  width="250"/>
    - Follow these steps if you own an app:
        1. Select **App**. 
        2. Enter the **App URL**. 
        3. Provide your app's **Test Account credentials**. If the customer does not need to Log in to your app, select **My app doesn’t require log in to transact**.
        4. Click **Submit app for review**.
            <img class="click-zoom" src="/docs/assets/images/dashboard-guide-myaccount-profile-update-app.jpg" alt="Enter App URL"  width="250"/>

After the details are provided, our team will review the request. We will update the details on the Dashboard.


</show-if>


<show-if org="razorpay" country="IN">

To update the website or mobile app details:
1. Log in to the Dashboard.
2. Click **Account & Settings** in the left navigation.
1. Click **Business website detail** under the **Website and app settings** section.
3. Click the edit icon next to the **Business Website/App details** field.
4. In the pop-up page that is displayed, click **Proceed to update website/app**.
5. Provide the website or app details:
    - Follow these steps if you own a website:
        1. Select **Website**.
        2. Enter the **Website URL**. 
        3. Provide the links for these pages: **About us**, **Contact us**, **Pricing details**, **Terms and conditions**, **Privacy policy** and **Refunds policy**. 
        4. Provide your website's **Test Account credentials**. If the customer does not need to Log in to your website, select **My website doesn’t require log in to transact**.
        5. Click **Submit website for review**.

    - Follow these steps if you own an app:
        1. Select **App**. 
        2. Enter the **App URL**. 
        3. Provide your app's **Test Account credentials**. If the customer does not need to Log in to your app, select **My app doesn’t require log in to transact**.
        4. Click **Submit app for review**.

After the details are provided, our team will review the request. We will update the details on the Dashboard.


</show-if>

<show-if org="razorpay" country="MY">

To update website or mobile app details:
1. Log in to the <a href="https://dashboard.curlec.com/?screen=sign_in" target="_blank">Curlec Dashboard</a>.
2. Navigate to **Account & Settings** → **Profile**.
3. Click the edit icon next to the **Business Website/App details** field.
    <img class="click-zoom" src="/docs/assets/images/dashboard-guide-myaccount-profile-update.jpg" alt="Update your website from Curlec Dashboard"  width="800"/>
4. In the pop-up page that is displayed, click **Proceed to update website/app**.
5. Provide the website or app details:
    - Follow these steps if you own a website:
        1. Select **Website**.
        2. Enter the **Website URL**. 
        3. Provide the links for these pages: **About us**, **Contact us**, **Pricing details**, **Terms and conditions**, **Privacy policy** and **Refunds policy**. 
        4. Provide your website's **Test Account credentials**. If the customer does not need to Log in to your website, select **My website doesn’t require log in to transact**.
        5. Click **Submit website for review**.
             <img class="click-zoom" src="/docs/assets/images/dashboard-guide-myaccount-profile-update-website-url.jpg" alt="Enter Website URL"  width="250"/>
    - Follow these steps if you own an app:
        1. Select **App**. 
        2. Enter the **App URL**. 
        3. Provide your app's **Test Account credentials**. If the customer does not need to Log in to your app, select **My app doesn’t require log in to transact**.
        4. Click **Submit app for review**.
            <img class="click-zoom" src="/docs/assets/images/dashboard-guide-myaccount-profile-update-app.jpg" alt="Enter App URL"  width="250"/>

After the details are provided, our team will review the request. We will update the details on the Dashboard.

<img class="click-zoom" src="/docs/assets/images/dashboard-guide-myaccount-profile-update-pending.jpg" alt="The updated website/mobile app details is under review"  width="600"/>

</show-if>

<callout info>
**Handy Tips**

We may reach out to you for clarifications via email, WhatsApp, SMS, and <brand-name/> Dashboard during the verification process.
Navigate to **Account & Settings** → **Profile** and submit the necessary information in the appropriate section. Our team will go through the information you provide and help you resolve the issue.
</callout>

# Add or Update Additional Website Details
You can accept payments using your <brand-name/> account on more than one website. To do this, you need to share with us the details of the additional web pages.

<callout info>
**Handy Tips**

This feature is available only if your services/products fall under the e-commerce business category.
</callout>

<show-if org="razorpay" country="IN">

To add an additional website:
1. Log in to the <a href="https://dashboard.razorpay.com/#/app" target="_blank">Razorpay Dashboard</a>.
1. Click **Account & Settings** in the left navigation.
1. Click **Business website detail** under **Website and app settings** section.
1. Click the plus icon next to the **Additional Business Website/App** field.
    <img class="click-zoom" src="/docs/assets/images/dashboard-guide-myaccount-profile-update-website.jpg" alt="Add additional business website or app"  width="800"/>
1. In the pop-up page that is displayed, click **Proceed to update website/app**.
    <img class="click-zoom" src="/docs/assets/images/dashboard-guide-myaccount-profile-additional-website.jpg" alt="Proceed to update website or app" width="300"/>
1. Provide the website or app details:
    - Follow these steps if you own a website:
        1. Select **Website**.
        2. Enter the **Website URL**. 
        3. Provide the links for these pages: **About us**, **Contact us**, **Pricing details**, **Terms and conditions**, **Privacy policy** and **Cancellation/Refund policy**. 
            <img class="click-zoom" src="/docs/assets/images/dashboard-guide-myaccount-profile-additional-website-links.jpg" alt="Enter additional website URL and details"  width="350"/>
        4. **Upload invoice**: Upload a sample invoice. The accepted file formats are PNG, JPG and PDF.
        5. **Reason for adding new website**: Enter the reason for adding a new website. Enter a minimum of 50 words.
        6. Provide your website's **Test Account credentials** if required or select **My website doesn’t require log in to transact** check box if logging in is not required. 
        7. Click **Submit website for review**.
             <img class="click-zoom" src="/docs/assets/images/dashboard-guide-myaccount-profile-additional-website-submit.jpg" alt="Upload invoice and submit reason for adding new website"  width="350"/>
    - Follow these steps if you own an app:
        1. Select **App**. 
        2. Enter the **App URL**. 
        3. **Reason for adding new website**: Enter the reason for adding a new website. Enter a minimum of 50 words.
        4. Provide your app's **Test Account credentials** if required or select **My app doesn’t require log in to transact** check box if logging in is not required. 
        5. Click **Submit app for review**.
             <img class="click-zoom" src="/docs/assets/images/dashboard-guide-myaccount-profile-additional-app.jpg" alt="Enter app URL and submit reason for adding new app" width="350"/>

After you provide the details, our team will review the request. We will update the details on the Dashboard.
<img class="click-zoom" src="/docs/assets/images/dashboard-guide-myaccount-profile-additional-app-pending.jpg" alt="Additional website added or updated is under review"  width="800"/>

</show-if>

<show-if org="axis">

To add an additional website:
1. Log in to the Dashboard.
1. Click **Account & Settings** in the left navigation.
1. Click **Business website detail** under the **Website and app settings** section.
1. Click the plus icon next to the **Additional Business Website/App** field.
1. In the pop-up page that is displayed, click **Proceed to update website/app**.
1. Provide the website or app details:
    - Follow these steps if you own a website:
        1. Select **Website**.
        2. Enter the **Website URL**. 
        3. Provide the links for these pages: **About us**, **Contact us**, **Pricing details**, **Terms and conditions**, **Privacy policy** and **Cancellation/Refund policy**. 
        4. **Upload invoice**: Upload a sample invoice. The accepted file formats are PNG, JPG and PDF.
        5. **Reason for adding new website**: Enter the reason for adding a new website. Enter a minimum of 50 words.
        6. Provide your website's **Test Account credentials** if required or select **My website doesn’t require log in to transact** check box if logging in is not required. 
        7. Click **Submit website for review**.

    - Follow these steps if you own an app:
        1. Select **App**. 
        2. Enter the **App URL**. 
        3. **Reason for adding new website**: Enter the reason for adding a new website. Enter a minimum of 50 words.
        4. Provide your app's **Test Account credentials** if required or select **My app doesn’t require log in to transact** check box if logging in is not required. 
        5. Click **Submit app for review**.

After you provide the details, our team will review the request. We will update the details on the Dashboard.

</show-if>


<show-if org="razorpay" country="MY">

To add additional website:
1. Log in to the <a href="https://dashboard.curlec.com/?screen=sign_in" target="_blank">Curlec Dashboard</a>.
2. Navigate to **Account & Settings** → **Profile**.
3. Click the icon next to the **Additional Business Website/App** field.
4. In the pop-up page that is displayed, click **Proceed to update website/app**.
5. Provide the website or app details:
    - Follow these steps if you own a website:
        1. Select **Website**.
        2. Enter the **Website URL**. 
        3. Provide the links for these pages: **About us**, **Contact us**, **Pricing details**, **Terms and conditions**, **Privacy policy** and **Cancellation/Refund policy**.
        4. **Upload invoice**: Upload a sample invoice. The accepted file formats are PNG, JPG and PDF.
        5. **Reason for adding new website**: Enter the reason for adding a new website. Enter a minimum of 50 words.
        6. Provide your website's **Test Account credentials** if required or select **My website doesn’t require log in to transact** check box if logging in is not required. 
        7. Click **Submit website for review**.
             <img class="click-zoom" src="/docs/assets/images/dashboard-guide-myaccount-profile-additional-website-submit.jpg" alt="Upload invoice and submit reason for adding new website"  width="350"/>
    - Follow these steps if you own an app:
        1. Select **App**. 
        2. Enter the **App URL**. 
        3. **Reason for adding new website**: Enter the reason for adding a new website. Enter a minimum of 50 words.
        4. Provide your app's **Test Account credentials** if required or select **My app doesn’t require log in to transact** check box if logging in is not required. 
        5. Click **Submit app for review**.
             <img class="click-zoom" src="/docs/assets/images/dashboard-guide-myaccount-profile-additional-app.jpg" alt="Enter app URL and submit reason for adding new app" width="350"/>

After you provide the details, our team will review the request. We will update the details on the Dashboard.
<img class="click-zoom" src="/docs/assets/images/dashboard-guide-myaccount-profile-additional-app-pending.jpg" alt="Additional website added or updated is under review"  width="800"/>

</show-if>

# Update Limit per Domestic Transaction

<show-if org="razorpay" country="IN">

You can update the domestic transaction limit for your Razorpay account. For example, if you could accept only ₹50,000 per transaction, you can update it to a higher amount, such as ₹1,00,000.

</show-if>

<show-if org="razorpay" country="MY">

You can update the domestic transaction limit for your Curlec account. For example, if you could accept only `RM50,000` per transaction, you can update it to a higher amount, such as `RM1,00,000`.

</show-if>

<callout warn>
**Watch Out**

The ceiling amount differs on the basis of your business category.
</callout>

<show-if org="razorpay" country="IN">

To update your per domestic transaction limit:
1. Log in to the <a href="https://dashboard.razorpay.com/#/app" target="_blank">Razorpay Dashboard</a>.
2. Click **Account & Settings** in the left navigation.
1. Click **Transaction limits** under **Payment and refund** section.
3. Click the edit icon next to the **Limit per domestic transaction** field.
    <img class="click-zoom" src="/docs/assets/images/dashboard-guide-myaccount-profile-transaction-limit.jpg" alt="Update the per domestic transaction limit"  width="800"/>
4. In the pop-up page that is displayed, provide the following information:
    1. **Required Limit**: Enter the desired per transaction limit amount. 
    2. **Why do you want to increase limit?**: Enter the reason you want to increase the per domestic transaction limit. You should enter a minimum of 100 words.
    3. **Upload invoice**: Upload a sample invoice. The accepted file formats are PNG, JPG and PDF.
    4. Click **Submit Details**.
        <img class="click-zoom" src="/docs/assets/images/dashboard-guide-myaccount-profile-transaction-limit-submit.jpg" alt="Provide invoice to update the limit per domestic transaction"  width="300"/>

After the details are provided, our team will review the request. We will update the details on the Dashboard.

</show-if>

<show-if org="axis">

To update your per domestic transaction limit:
1. Log in to the Dashboard.
2. Click **Account & Settings** in the left navigation.
1. Click **Transaction limits** under **Payment and refund** section.
3. Click the edit icon next to the **Limit per domestic transaction** field.
4. In the pop-up page that is displayed, provide the following information:
    1. **Required Limit**: Enter the desired per transaction limit amount. 
    2. **Why do you want to increase limit?**: Enter the reason you want to increase the per domestic transaction limit. You should enter a minimum of 100 words.
    3. **Upload invoice**: Upload a sample invoice. The accepted file formats are PNG, JPG and PDF.
    4. Click **Submit Details**.

After the details are provided, our team will review the request. We will update the details on the Dashboard.

</show-if>

<show-if org="razorpay" country="MY">

To update your per domestic transaction limit:
1. Log in to the <a href="https://dashboard.curlec.com/?screen=sign_in" target="_blank">Curlec Dashboard</a>.
2. Navigate to **Account & Settings** → **Profile**.
3. Click the edit icon next to the **Limit per domestic transaction** field.
4. In the pop-up page that is displayed, provide the following information:
    1. **Required Limit**: Enter the desired per transaction limit amount. 
    2. **Why do you want to increase limit?**: Enter the reason you want to increase the per domestic transaction limit. You should enter a minimum of 100 words.
    3. **Upload invoice**: Upload a sample invoice. The accepted file formats are PNG, JPG and PDF.
    4. Click **Submit Details**.

After the details are provided, our team will review the request. We will update the details on the Dashboard.

</show-if>

<callout info>
**Handy Tips**

We may reach out to you for clarifications on email, WhatsApp, SMS, and <brand-name/> Dashboard during the verification process.
Navigate to **Account & Settings** → **Profile** and submit the necessary information in the appropriate section. Our team will go through the information you provide and help you resolve the issue.
</callout>

<show-if org="razorpay" country="IN">

# Update Limit per International Transaction

You can update the international transaction limit for your Razorpay account. For example, if you could accept only ₹50,000 per transaction, you can update it to a higher amount, such as ₹1,00,000.


<callout warn>
**Watch Out**

The ceiling amount differs on the basis of your business category.
</callout>

</show-if>

<show-if org="razorpay" country="IN">

To update your per international transaction limit:
1. Log in to the <a href="https://dashboard.razorpay.com/#/app" target="_blank">Razorpay Dashboard</a>.
2. Click **Account & Settings** in the left navigation.
1. Click **Transaction limits** under **Payment and refund** section.
3. Click the edit icon next to the **Limit per international transaction** field.
    <img class="click-zoom" src="/docs/assets/images/profile-international-transaction-limit.jpg" alt="Update limit per international transaction"  width="800"/>
4. In the pop-up page that is displayed, provide the following information:
    1. **Required Limit**: Enter the desired per transaction limit amount. 
    2. **Why do you want to increase limit?**: Enter the reason you want to increase the per international transaction limit. You should enter a minimum of 100 words.
    3. **Upload invoice**: Upload a sample invoice. The accepted file formats are PNG, JPG and PDF.
    4. Click **Submit Details**.
        <img class="click-zoom" src="/docs/assets/images/international-transaction-limit-submit.jpg" alt="Provide invoice to update limit per international transaction"  width="500"/>

After the details are provided, our team will review the request. We will update the details on the Dashboard.



<callout info>
**Handy Tips**

We may reach out to you for clarifications on email, WhatsApp, SMS, and <brand-name/> Dashboard during the verification process.
Navigate to **Account & Settings** → **Profile** and submit the necessary information in the appropriate section. Our team will go through the information you provide and help you resolve the issue.
</callout>

</show-if>

# Update Brand Name

<show-if org="razorpay" country="IN">

You can update the brand name displayed to your customers in the following places:
- On transaction and refund emails sent to customers.
- On the links sent to customers for **Payment Links**, **Payment Pages**, **Invoices** and **Subscriptions**.
- As the beneficiary name when you create a **Smart Collect** Customer Identifier. Know more about <a href="/docs/smart-collect" target="_blank">Smart Collect</a>.

</show-if>

<show-if org="axis">

You can update the brand name displayed to your customers in the following places:
- On transaction and refund emails sent to customers.
- On the links sent to customers for **Payment Links**, **Payment Pages**, **Invoices** and **Subscriptions**.
- As the beneficiary name when you create a **Smart Collect** Customer Identifier. Know more about <a href="/docs/smart-collect" target="_blank">Smart Collect</a>.

</show-if>

<show-if org="razorpay" country="MY">

You can update the brand name displayed to your customers in the following places:
- On transaction and refund emails sent to customers.
- On the links sent to customers for **Payment Links**, **Payment Pages** and **Invoices**.

</show-if>

### Example
While creating the <brand-name/> account, you provided the name as **Acme Corp**; now, you want to change it to **Acme Co**.

<callout info>
**Handy Tips**

- This feature is available only for the registered <brand-name/> users.
- Only users with 'Owner' or 'Admin' roles can update the brand name.
- Bank-related SMS or credit card statements sent to customers will not have the brand name since these are managed by the banks and not <brand-name/>. Such communication will display the billing name provided by you during account creation and activation process.
</callout>

<show-if org="razorpay" country="IN">

To update your brand name:
1. Log in to the <a href="https://dashboard.razorpay.com/#/app" target="_blank">Razorpay Dashboard</a>.
2. Click **Account & Settings** in the left navigation.
1. Click **Business details** under **Business settings** section.
3. Click the edit icon in the **Brand Name** field.
4. A list of recommended brand names appear.
    - Select one of the names from the list, or
    - Enter a custom brand name. Ensure that the custom name you are entering is similar to the business name or your business website domain.
5. Click **Save Changes**.

The brand name appears updated on the Dashboard and will reflect on all the above-mentioned places.

</show-if>

<show-if org="axis">

To update your brand name:
1. Log in to the Dashboard.
2. Click **Account & Settings** in the left navigation.
1. Click **Business details** under **Business settings** section.
3. Click the edit icon in the **Brand Name** field.
4. A list of recommended brand names appear.
    - Select one of the names from the list, or
    - Enter a custom brand name. Ensure that the custom name you are entering is similar to the business name or your business website domain.
5. Click **Save Changes**.

The brand name appears updated on the Dashboard and will reflect on all the above-mentioned places.

</show-if>

<show-if org="razorpay" country="MY">

To update your brand name:
1. Log in to the <a href="https://dashboard.curlec.com/?screen=sign_in" target="_blank">Curlec Dashboard</a>.
2. Navigate to **Account & Settings** → **Profile**.
3. Click the edit icon in the **Brand Name** field.
4. A list of recommended brand names appear.
    - Select one of the names from the list, or
    - Enter a custom brand name. Ensure that the custom name you are entering is similar to the business name or your business website domain.
5. Click **Save Changes**.

The brand name appears updated on the Dashboard and will reflect on all the above-mentioned places.

</show-if>

<show-if org="razorpay" country="IN">

# Update Importer-Exporter Code (IEC)

You can update the Importer-Exporter Code on the Razorpay Dashboard.
- The IEC is a code issued by the Indian Director General of Foreign Trade (DGFT) to Indian companies to export goods from India. You can apply for an IEC from the <a href="https://dgft.gov.in/CP/" target="_blank">DGFT website</a>.
- Submit your IEC if you have one, sell physical goods, or sell services and utilise certain benefits under India’s Foreign Trade Policy.

<callout info>
**Handy Tips**

This feature is available only for Razorpay users who accept international payments and export goods.
</callout>

To update your IEC Code:
1. Log in to the <a href="https://dashboard.razorpay.com/#/app" target="_blank">Razorpay Dashboard</a>.
2. Click **Account & Settings** in the left navigation.
3. Click **Select Code** next to the **Purpose Code** field.
4. A list of Purpose Codes appear. Select a Purpose Code and click **Next**.
5. Enter the 10-digit IEC and click **Next**.
6. Review and click **Confirm**.

The Purpose Code and IEC appear updated on the Dashboard.

</show-if>