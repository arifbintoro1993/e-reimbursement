from rest_framework import serializers
from django_multitenant.models import get_current_tenant

from e_reimbursement.reimbursement.models import Reimbursement


class ReimbursementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reimbursement
        fields = ("pk", "date_of_purchase", "category", "description", "amount", "attachment", "status")
        extra_kwargs = {
            "reject_url": {
                "view_name": "api:reimbursement-reject", "lookup_field": "pk"
            },
            "accept_url": {
                "view_name": "api:reimbursement-accept", "lookup_field": "pk"
            }
        }

    def create(self, validated_data):
        reimbursement_data = {
            "date_of_purchase": validated_data.pop("date_of_purchase"),
            "category": validated_data.pop("category"),
            "description": validated_data.pop("description"),
            "amount": validated_data.pop("amount"),
            "attachment": validated_data.pop("attachment"),
            "status": validated_data.pop("status"),
            "employee": get_current_tenant()

        }
        reimbursement = Reimbursement.objects.create(**reimbursement_data)
        return reimbursement
