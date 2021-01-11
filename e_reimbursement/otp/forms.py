from django import forms
from django.utils.translation import ugettext_lazy as _


class OTPVerificationForm(forms.Form):
    token = forms.IntegerField(
        label=_("Token"), min_value=1, max_value=6
    )
    reimbursement_pk = forms.CharField(widget=forms.HiddenInput)
