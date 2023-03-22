---
title: Payments Dashboard | Manage Team
razorpay-MY-title: Payments Dashboard | Manage Team
heading: Manage Team
razorpay-MY-heading: Manage Team
desc: Mange your team, add or remove users and provide appropriate roles to control access.
razorpay-MY-desc: Mange your team, add or remove users and provide appropriate roles to control access.
---

You can manage your team of users who can access the <brand-name/> Dashboard. You can provide specific access to a user or a set of users.

### Example
You need someone in your organisation to perform day-to-day operations such as handling refunds and settlements. In this case, you can give <brand-name/> Dashboard access to a person and assign the **Operations** role. This limits their access to actions related to refunds and settlements only.

# Standard User Roles
There are some predefined user roles that you can assign to your team members. You can use these roles to limit a user's access to the Dashboard. The below table explains each role and the permissions associated with it. A team member should be assigned a role as the role is tied to an email address. A user can have multiple roles if they have different email ids.

<show-if org="razorpay" country="IN">

<table>
Role | Action Allowed | Actions not Allowed
---
Owner | <ul><li>Generate API Keys.</li><li>Create and manage webhooks.</li><li>Manage Teams.</li><li>Update brand name.</li><li>Edit activation form details, including bank account details and GST number, before submission.</li><li>View all transactions and settlements.</li><li>View all disputes.</li><li>Accept all disputes.<li>Contest all disputes and submit evidence.</li></li><li>Configure payment capture settings.</li><li>Configure payment methods.</li><li>Capture transactions.</li><li>Create refunds.</li><li>Create and manage Invoices, Payment Pages, Payment Links, Plans and Subscription Links, Customers and Virtual Accounts.</li><li>Edit linked account details.</li><li>Create and upload batch files.</li><li>Download and email reports.</li><li>Use Payments Mobile App.</li><li>Create Offers.</li><li>Install OAuth Apps.</li></ul>| NA
---
Admin | <ul><li>Generate API Keys.</li><li>Create and manage webhooks.</li><li>Update brand name.</li><li>Edit activation form details, including bank account details and GST number, before submission.</li><li>Configure payment methods.</li><li>View all transactions and settlements.</li><li>View all disputes.</li><li>Accept all disputes.</li><li>Contest all disputes and submit evidence.</li><li>Capture transactions.</li><li>Create refunds.</li><li>Create and manage Invoices, Payment Pages, Payment Links, Plans and Subscription Links, Customers and Virtual Accounts.</li><li>Create and upload batch files.</li><li>Download and email reports.</li><li>Use Payments Mobile App.</li><li>Create Offers.</li><li>Edit linked account details.</li></ul> | <ul><li>Manage Teams.</li></ul>
---
Manager | <ul><li>Create and manage webhooks.</li><li>Edit activation form details, including GST number, before submission.</li><li>Configure payment capture settings.</li><li>Configure payment methods.</li><li>View all transactions and settlements.</li><li>View all disputes.</li><li>Accept all disputes.</li><li>Contest all disputes and submit evidence.</li><li>Capture transactions.</li><li>Create refunds.</li><li>Create and manage Invoices, Payment Pages, Payment Links, Plans and Subscription Links, Customers and Virtual Accounts.</li><li>Create and upload batch files.</li><li>Download and email reports. </li><li>Use Payments Mobile App.</li><li>Edit linked account details.</li></ul> | <ul><li>Generate API Keys.</li><li>Manage Teams.</li><li>Resend Subscription Registration link</li></ul>
---
Operations | <ul><li>View all transactions and settlements.</li><li>View all disputes.</li><li>Accept all disputes.</li><li>Contest all disputes and submit evidence.</li><li>Capture transactions. </li><li>Create refunds. </li><li>Create Invoices, Payment Links, Payment Pages, Payment Buttons and Virtual Accounts.</li><li>Create and upload batch files.</li><li>Download and email reports. </li><li>Use Payments Mobile App.</li></ul> | <ul><li>Generate API Keys.</li><li>Manage Teams.</li><li>Edit activation form details, including bank account details and GST number, before submission.</li><li>Edit linked account details.</li></ul>
---
Finance | <ul><li>Edit activation form details including GST number, before submission.</li><li>View all transactions and settlements.</li><li>View all disputes.</li><li>Accept all disputes.</li><li>Contest all disputes and submit evidence.</li><li>Create and upload batch files.</li><li>Download and email reports.</li></ul> | <ul><li>Generate API Keys.</li><li>Create and manage webhooks.</li><li>Manage Teams.</li><li>Capture transactions.</li><li>Create refunds.</li><li>Create and manage Invoices, Payment Pages, Payment Links, Plans and Subscription Links, Customers and Virtual Accounts.</li><li>Edit linked account details.</li></ul>
---
ePos | <ul><li>Create Invoices and Payment Links in INR only.</li><li>Create, view and edit Offers.</li></ul> | <ul><li>Generate API Keys.</li><li>Edit activation form details including GST number, before submission.</li><li>Create and manage webhooks.</li><li>Manage Teams.</li><li>View all transactions and settlements.</li><li>View all disputes.</li><li>Accept all disputes.</li><li>Contest all disputes and submit evidence.</li><li>Capture transactions.</li><li>Create refunds.</li><li>Edit linked account details.</li><li>Create and upload batch files.</li><li>Download and email reports.</li><li>Create Items.</li><li>View Invoices, Payment Pages, Payment Links created by other users.</li></ul>
---
Support | <ul><li>View all transactions and settlements.</li><li>View all disputes.</li><li>Accept all disputes.</li><li>Download and email reports other than the monthly invoice report.</li></ul> | <ul><li>Generate API Keys.</li><li>Create and manage webhooks.</li><li>Manage Teams.</li><li>Edit activation form details, including bank account details and GST number, before submission.</li><li>Capture transactions.</li><li>Create refunds.</li><li>Create and manage Invoices, Payment Pages, Payment Links, Plans and Subscription Links, Customers and Virtual Accounts.</li><li>Edit linked account details.</li><li>Create and upload batch files.</li><li>Access monthly invoice report.</li></ul>
</table>

</show-if>


<show-if org="axis">

<table>
Role | Action Allowed | Actions not Allowed
---
Owner | <ul><li>Generate API Keys.</li><li>Create and manage webhooks.</li><li>Manage Teams.</li><li>Update brand name.</li><li>Edit activation form details, including bank account details and GST number, before submission.</li><li>View all transactions and settlements.</li><li>View all disputes.</li><li>Accept all disputes.<li>Contest all disputes and submit evidence.</li></li><li>Configure payment capture settings.</li><li>Configure payment methods.</li><li>Capture transactions.</li><li>Create refunds.</li><li>Create and manage Invoices, Payment Pages, Payment Links, Plans and Subscription Links, Customers and Virtual Accounts.</li><li>Edit linked account details.</li><li>Create and upload batch files.</li><li>Download and email reports.</li><li>Use Payments Mobile App.</li><li>Create Offers.</li><li>Install OAuth Apps.</li></ul>| NA
---
Admin | <ul><li>Generate API Keys.</li><li>Create and manage webhooks.</li><li>Update brand name.</li><li>Edit activation form details, including bank account details and GST number, before submission.</li><li>Configure payment methods.</li><li>View all transactions and settlements.</li><li>View all disputes.</li><li>Accept all disputes.</li><li>Contest all disputes and submit evidence.</li><li>Capture transactions.</li><li>Create refunds.</li><li>Create and manage Invoices, Payment Pages, Payment Links, Plans and Subscription Links, Customers and Virtual Accounts.</li><li>Create and upload batch files.</li><li>Download and email reports.</li><li>Use Payments Mobile App.</li><li>Create Offers.</li><li>Edit linked account details.</li></ul> | <ul><li>Manage Teams.</li></ul>
---
Manager | <ul><li>Create and manage webhooks.</li><li>Edit activation form details, including GST number, before submission.</li><li>Configure payment capture settings.</li><li>Configure payment methods.</li><li>View all transactions and settlements.</li><li>View all disputes.</li><li>Accept all disputes.</li><li>Contest all disputes and submit evidence.</li><li>Capture transactions.</li><li>Create refunds.</li><li>Create and manage Invoices, Payment Pages, Payment Links, Plans and Subscription Links, Customers and Virtual Accounts.</li><li>Create and upload batch files.</li><li>Download and email reports. </li><li>Use Payments Mobile App.</li><li>Edit linked account details.</li></ul> | <ul><li>Generate API Keys.</li><li>Manage Teams.</li><li>Resend Subscription Registration link</li></ul>
---
Operations | <ul><li>View all transactions and settlements.</li><li>View all disputes.</li><li>Accept all disputes.</li><li>Contest all disputes and submit evidence.</li><li>Capture transactions. </li><li>Create refunds. </li><li>Create Invoices, Payment Links, Payment Pages, Payment Buttons and Virtual Accounts.</li><li>Create and upload batch files.</li><li>Download and email reports. </li><li>Use Payments Mobile App.</li></ul> | <ul><li>Generate API Keys.</li><li>Manage Teams.</li><li>Edit activation form details, including bank account details and GST number, before submission.</li><li>Edit linked account details.</li></ul>
---
Finance | <ul><li>Edit activation form details including GST number, before submission.</li><li>View all transactions and settlements.</li><li>View all disputes.</li><li>Accept all disputes.</li><li>Contest all disputes and submit evidence.</li><li>Create and upload batch files.</li><li>Download and email reports.</li></ul> | <ul><li>Generate API Keys.</li><li>Create and manage webhooks.</li><li>Manage Teams.</li><li>Capture transactions.</li><li>Create refunds.</li><li>Create and manage Invoices, Payment Pages, Payment Links, Plans and Subscription Links, Customers and Virtual Accounts.</li><li>Edit linked account details.</li></ul>
---
ePos | <ul><li>Create Invoices and Payment Links in INR only.</li><li>Create, view and edit Offers.</li></ul> | <ul><li>Generate API Keys.</li><li>Edit activation form details including GST number, before submission.</li><li>Create and manage webhooks.</li><li>Manage Teams.</li><li>View all transactions and settlements.</li><li>View all disputes.</li><li>Accept all disputes.</li><li>Contest all disputes and submit evidence.</li><li>Capture transactions.</li><li>Create refunds.</li><li>Edit linked account details.</li><li>Create and upload batch files.</li><li>Download and email reports.</li><li>Create Items.</li><li>View Invoices, Payment Pages, Payment Links created by other users.</li></ul>
---
Support | <ul><li>View all transactions and settlements.</li><li>View all disputes.</li><li>Accept all disputes.</li><li>Download and email reports other than the monthly invoice report.</li></ul> | <ul><li>Generate API Keys.</li><li>Create and manage webhooks.</li><li>Manage Teams.</li><li>Edit activation form details, including bank account details and GST number, before submission.</li><li>Capture transactions.</li><li>Create refunds.</li><li>Create and manage Invoices, Payment Pages, Payment Links, Plans and Subscription Links, Customers and Virtual Accounts.</li><li>Edit linked account details.</li><li>Create and upload batch files.</li><li>Access monthly invoice report.</li></ul>
</table>

</show-if>


<show-if org="razorpay" country="MY">

<table>
Role | Action Allowed | Actions not Allowed
---
Owner | <ul><li>Generate API Keys.</li><li>Create and manage webhooks.</li><li>Manage Teams.</li><li>Update brand name.</li><li>Edit activation form details, including bank account details, before submission.</li><li>View all transactions and settlements.</li><li>Configure payment capture settings.</li><li>Configure payment methods.</li><li>Capture transactions.</li><li>Create refunds.</li><li>Create and manage Invoices, Payment Pages, Payment Links and Customers.</li><li>Create and upload batch files.</li><li>Download and email reports.</li><li>Install OAuth Apps.</li></ul>| NA
---
Admin | <ul><li>Generate API Keys.</li><li>Create and manage webhooks.</li><li>Update brand name.</li><li>Edit activation form details, including bank account details, before submission.</li><li>Configure payment methods.</li><li>View all transactions and settlements.</li><li>Capture transactions.</li><li>Create refunds.</li><li>Create and manage Invoices, Payment Pages, Payment Links and Customers.</li><li>Create and upload batch files.</li><li>Download and email reports.</li></ul> | <ul><li>Manage Teams.</li></ul>
---
Manager | <ul><li>Create and manage webhooks.</li><li>Edit activation form details, before submission.</li><li>Configure payment capture settings.</li><li>Configure payment methods.</li><li>View all transactions and settlements.</li><li>Capture transactions.</li><li>Create refunds.</li><li>Create and manage Invoices, Payment Pages, Payment Links and Customers.</li><li>Create and upload batch files.</li><li>Download and email reports. </li></ul> | <ul><li>Generate API Keys.</li><li>Manage Teams.</li></ul>
---
Operations | <ul><li>View all transactions and settlements.</li><li>Capture transactions. </li><li>Create refunds. </li><li>Create Invoices, Payment Links, Payment Pages and Payment Buttons.</li><li>Create and upload batch files.</li><li>Download and email reports. </li></ul> | <ul><li>Generate API Keys.</li><li>Manage Teams.</li><li>Edit activation form details, including bank account details, before submission.</li></ul>
---
Finance | <ul><li>Edit activation form details, before submission.</li><li>View all transactions and settlements.</li><li>Create and upload batch files.</li><li>Download and email reports.</li></ul> | <ul><li>Generate API Keys.</li><li>Create and manage webhooks.</li><li>Manage Teams.</li><li>Capture transactions.</li><li>Create refunds.</li><li>Create and manage Invoices, Payment Pages, Payment Links and Customers.</li></ul>
---
Support | <ul><li>View all transactions and settlements.</li><li>Download and email reports other than the monthly invoice report.</li></ul> | <ul><li>Generate API Keys.</li><li>Create and manage webhooks.</li><li>Manage Teams.</li><li>Edit activation form details, including bank account details, before submission.</li><li>Capture transactions.</li><li>Create refunds.</li><li>Create and manage Invoices, Payment Pages, Payment Links and Customers.</li><li>Create and upload batch files.</li><li>Access monthly invoice report.</li></ul>
</table>

</show-if>

# Invite a User
You can invite anyone with a valid email address to your <brand-name/> account. Every user has unique login credentials.

## Invite a Registered User

<show-if org="razorpay" country="IN">

Watch this video to see how you can invite users to your team. <br/><br/>
<iframe width="560" height="315" src="https://www.youtube.com/embed/jqMrGbFCCi8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. Log in to the <a href="https://dashboard.razorpay.com" target="_blank">Razorpay Dashboard</a>.
2. Navigate to the **Account & Settings** tab and click **Manage Team**.
3. Type in the email address of the user whom you want to invite. Select a role from the drop-down list.
4. Click **Send Invitation** to invite the user. A list of accepted and pending invitations is displayed on the same page.
5. Click **Resend** to re-invite the user or **Cancel** to cancel the invitation.

</show-if>

<show-if org="axis">

1. Log in to the <a href="https://axis.razorpay.com/" target="_blank">Dashboard</a>.
2. Navigate to the **Account & Settings** tab and click **Manage Team**.
3. Type in the email address of the user whom you want to invite. Select a role from the drop-down list.
4. Click **Send Invitation** to invite the user. A list of accepted and pending invitations is displayed on the same page.
5. Click **Resend** to re-invite the user or **Cancel** to cancel the invitation.

</show-if>

<show-if org="razorpay" country="MY">

1. Log in to the <a href="https://dashboard.curlec.com/?screen=sign_in" target="_blank">Curlec Dashboard</a>.
2. Navigate to the **Account & Settings** tab and click **Manage Team**.
3. Type in the email address of the user whom you want to invite. Select a role from the drop-down list.
4. Click **Send Invitation** to invite the user. A list of accepted and pending invitations is displayed on the same page.
5. Click **Resend** to re-invite the user or **Cancel** to cancel the invitation.

</show-if>



## Accept Invite - Existing Razorpay User

<show-if org="razorpay" country="IN">

Watch this video to see how to accept an invite to be a team member.

<iframe width="560" height="315" src="https://www.youtube.com/embed/oGoWCOf6-Qo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

</show-if>

To accept an invite:
1. Log in to the Dashboard.
2. Navigate to the **Account & Settings** tab and click **Invitations**.
3. Click **Accept** next to the invite.

<show-if org="razorpay" country="IN">

<img class="click-zoom" src="/docs/assets/images/dashboard-guide-accept-invitation.jpg" alt="Accept invite to be team member (for an existing Razorpay user)" width='800'/>

</show-if>

<callout info>
**Switching Accounts**

After accepting the invite, the invited user can switch between their and your account using the **Switch Merchant** option available on the Dashboard header.
You cannot access their account unless they invite you to join their team.
</callout>


## Invite a New User

You can invite a user who is not registered with <brand-name/> to join your team. Such users are sent an invite link via email.

To invite a new user:

1. Log in to the Dashboard.
2. Click **Account & Settings** and go to **Manage team**.
3. Click **Invite New Member**.
4. Enter the member's email id and select the user role to be assigned.
5. Click **Send Invitation**.

<show-if org="razorpay" country="IN">

<img src="/docs/assets/images/dashboard-guide-invite-new-user.jpg" alt="/
Send invite to new member (for a new Razorpay user)" width='600'/>

</show-if>

# Update Role of a User

You can change the user's role after the invitation is sent to the user or after the invitation is accepted by the user.

<show-if org="razorpay" country="IN">

Watch this video to see how you can update the role of a user.

<iframe width="560" height="315" src="https://www.youtube.com/embed/UMEEFgTMB5k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

To update a user's role:
1. Log in to your <a href="https://dashboard.razorpay.com/#/access/signin" target="_blank">Razorpay Dashboard</a>.
2. Navigate to **Account & Settings** and click **Manage Team**.
3. Select the new role for the user from the dropdown.
4. Click **Update**.

</show-if>

<show-if org="axis">

To update a user's role:
1. Log in to your <a href="https://axis.razorpay.com/" target="_blank">Dashboard</a>.
2. Navigate to **Account & Settings** and click **Manage Team**.
3. Select the new role for the user from the dropdown.
4. Click **Update**.

</show-if>

<show-if org="razorpay" country="MY">

To update a user's role:
1. Log in to your <a href="https://dashboard.curlec.com/?screen=sign_in" target="_blank">Curlec Dashboard</a>.
2. Navigate to **Account & Settings** and click **Manage Team**.
3. Select the new role for the user from the dropdown.
4. Click **Update**.

</show-if>

# Remove a User
You can remove a user from your team to remove his/her complete access from your <brand-name/> Dashboard.

<show-if org="razorpay" country="IN">

Watch this video to see how you can remove a user from your team.

<iframe width="560" height="315" src="https://www.youtube.com/embed/H_IBGauvj1M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

To remove a user from your team:
1. Log in to your <a href="https://dashboard.razorpay.com/#/access/signin" target="_blank">Razorpay Dashboard</a>.
1. Navigate to **Account & Settings** and click **Manage Team**.
1. Click **Remove** to remove a user from the **Team Member** list. Once removed, the user can no longer access your Dashboard.
1. Click **Cancel** to remove a user from the **Pending Invitations** list.

</show-if>


<show-if org="axis">

To remove a user from your team:
1. Log in to your <a href="https://axis.razorpay.com/" target="_blank">Dashboard</a>.
1. Navigate to **Account & Settings** and click **Manage Team**.
1. Click **Remove** to remove a user from the **Team Member** list. Once removed, the user can no longer access your Dashboard.
1. Click **Cancel** to remove a user from the **Pending Invitations** list.

</show-if>

<show-if org="razorpay" country="MY">

To remove a user from your team:
1. Log in to your <a href="https://dashboard.curlec.com/?screen=sign_in" target="_blank">Curlec Dashboard</a>.
1. Navigate to **Account & Settings** and click **Manage Team**.
1. Click **Remove** to remove a user from the **Team Member** list. Once removed, the user can no longer access your Dashboard.
1. Click **Cancel** to remove a user from the **Pending Invitations** list.

</show-if>

# 2-Step Verification (Team Level)

You can set 2-step verification for your entire team for enhanced security and protection of your <brand-name/> Dashboard data thus preventing malicious attacks or misuse of your sensitive business data.

## What is 2-Step Account Verification (Two-factor Authentication, 2FA)

<callout info>
**Account 2-Step Verification**

Know about <a href="/docs/payment-gateway/dashboard-guide/profile/#2-step-verification" target="_blank">2-step verification</a>.
</callout>

<show-if org="razorpay" country="IN">

Watch this video to see how to enable 2FA for your entire team.

<iframe width="560" height="315" src="https://www.youtube.com/embed/2-1TdPA_7rA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

To enable 2-step verification for your team:
1. Log in to your <a href="https://dashboard.razorpay.com/#/access/signin" target="_blank">Razorpay Dashboard</a>.
2. Navigate to **Account & Settings** → **Manage Team**.
3. Enable the **2-Step Verification to the team** option.
4. Enter the OTP sent to your registered mobile device. (This step is not required if you had already performed OTP verification during login.)
5. Enter your account password and confirm.

You have now set up 2FA for your entire team.

</show-if>


<show-if org="axis">

To enable 2-step verification for your team:
1. Log in to your <a href="https://axis.razorpay.com/" target="_blank">Dashboard</a>.
1. Navigate to **Account & Settings** → **Manage Team**.
1. Enable the **2-Step Verification to the team** option.
1. Enter the OTP sent to your registered mobile device. (This step is not required if you had already performed OTP verification during login.)
1. Enter your account password and confirm.

You have now set up 2FA for your entire team.

</show-if>

<show-if org="razorpay" country="MY">

To enable 2-step verification for your team:
1. Log in to your <a href="https://dashboard.curlec.com/?screen=sign_in" target="_blank">Curlec Dashboard</a>.
2. Navigate to **Account & Settings** → **Manage Team**.
3. Enable the **2-Step Verification to the team** option.
4. Enter the OTP sent to your registered mobile device. (This step is not required if you had already performed OTP verification during login.)
5. Enter your account password and confirm.

You have now set up 2FA for your entire team.

</show-if>

# FAQs

#### 1. What to do if a user account is locked?
If a user enters the wrong OTP 9 times, their account will be locked for security reasons. In such scenarios, the user should contact their respective account owner. The account owner can unlock the users' accounts.

#### 2. What to do if a user loses their mobile device?
If a user loses their mobile device, they should reach out to their respective account owner. The account owner can **Invalidate 2FA** for the user, that is reset 2FA for the user. The user will be asked to enter their mobile number the next time they log in to the Dashboard.

<show-if org="razorpay" country="IN">
Watch this video to see how the owner can reset 2FA for a team member.<br/>

<iframe width="560" height="315" src="https://www.youtube.com/embed/6PWz3RMEdoo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

</show-if>

<show-if org="razorpay" country="IN">

#### 3. What to do if the account owner is locked?
If you are the account owner and have entered the wrong OTP 9 times, your account will be locked for security reasons. In such scenarios, contact our <a href="https://razorpay.com/support/#request" target="_blank">Support Team</a> to **Reset 2FA** for your account.

</show-if>

<show-if org="razorpay" country="MY">

#### 3. What to do if the account owner is locked?
If you are the account owner and have entered the wrong OTP 9 times, your account will be locked for security reasons. In such scenarios, contact our <a href="success@curlec.com">Support Team</a> to **Reset 2FA** for your account.

</show-if>

<show-if org="razorpay" country="IN">

#### 4. What to do if the account owner loses their mobile device?
If you are the account owner and have lost your mobile device, contact our <a href="https://razorpay.com/support/#request" target="_blank">Support Team</a> to **Reset 2FA** for your account.

</show-if>

<show-if org="razorpay" country="MY">

#### 4. What to do if the account owner loses their mobile device?
If you are the account owner and have lost your mobile device, contact our <a href="success@curlec.com">Support Team</a> to **Reset 2FA** for your account.

</show-if>