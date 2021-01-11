from django.views.generic import TemplateView

from e_reimbursement.reimbursement.api.serializers import ReimbursementSerializers


class ReimbursementListView(TemplateView):
    template_name = "reimbursement/reimbursement_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["serializer"] = ReimbursementSerializers
        return context
