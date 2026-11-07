from django import forms
from .models import Entry


class EntryForm(forms.ModelForm):
    agree = forms.BooleanField(
        required=True,
        label="I confirm that the information I have provided is accurate and agree to the Terms & Conditions and Privacy Notice.",
    )

    class Meta:
        model = Entry
        fields = [
            "first_name",
            "last_name",
            "date_of_birth",
            "email",
            "phone",
            "address_line_1",
            "address_line_2",
            "city",
            "county",
            "postcode",
            "paypal_email",
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "paypal_email": forms.EmailInput(attrs={"autocomplete": "email", "placeholder": "PayPal account email"}),
        }
