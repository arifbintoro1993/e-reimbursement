from django.views.generic import TemplateView
from django.db.models import Sum, Value
from django.db.models.functions import Coalesce


from e_reimbursement.reimbursement.api.serializers import ReimbursementSerializers
from e_reimbursement.otp.forms import OTPVerificationForm
from e_reimbursement.reimbursement.models import Reimbursement


class ReimbursementListView(TemplateView):
    template_name = "reimbursement/reimbursement_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["serializer"] = ReimbursementSerializers
        context["otp_verification_form"] = OTPVerificationForm
        context["transport"] = Reimbursement.objects.filter(
            category=Reimbursement.CATEGORY_CHOICES.transport
        ).aggregate(total=Coalesce(Sum("amount"), Value(0)))['total']
        context["fnb"] = Reimbursement.objects.filter(
            category=Reimbursement.CATEGORY_CHOICES.food_and_beverages
        ).aggregate(total=Coalesce(Sum("amount"), Value(0)))['total']
        context["office_supplies"] = Reimbursement.objects.filter(
            category=Reimbursement.CATEGORY_CHOICES.office_supplies
        ).aggregate(total=Coalesce(Sum("amount"), Value(0)))['total']

        print(context)
        return context
