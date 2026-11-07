# DBSEELY

DBSEELY means “Don't Be Silly.” This project uses the existing site layout and responsive styling under the DBSEELY brand. Gift-card content and gift-card assets have been removed.

## Run locally

1. Create and activate a virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Run database migrations: `python manage.py migrate`
4. Create an admin user: `python manage.py createsuperuser`
5. Start the development server: `python manage.py runserver`
6. Open `http://127.0.0.1:8000/`.

## Application data

The application stores the submitted contact details and PayPal account email in the Django database. The admin area lists applications and supports searching by applicant and PayPal email. The PayPal email is only a payout destination identifier; the site must never request PayPal passwords, one-time codes, or security answers.

## Important integrations not included

This project does not yet connect to PayPal Payouts or an identity-verification provider. No money is sent and no identity check is performed automatically. Before launching, configure a legitimate provider, obtain the required permissions, publish accurate Terms & Conditions and a Privacy Notice, and implement server-side eligibility/approval and payout handling. Do not use an unrelated third-party identity-check URL.

## Existing database

The source archive's local SQLite database was intentionally not copied into this project archive because it may contain personal application records. Run migrations against your own database. Migration `0005_replace_gift_card_with_paypal_email` removes the old gift-card preference field and adds `paypal_email`. Existing rows will need applicants to provide a PayPal email before they can be used for payouts.
