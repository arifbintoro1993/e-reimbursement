from django.views.generic import TemplateView

from e_reimbursement.reimbursement.api.serializers import ReimbursementSerializers
from e_reimbursement.otp.forms import OTPVerificationForm


class ReimbursementListView(TemplateView):
    template_name = "reimbursement/reimbursement_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["serializer"] = ReimbursementSerializers
        context["otp_verification_form"] = OTPVerificationForm
        return context
