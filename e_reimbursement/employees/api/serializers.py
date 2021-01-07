from rest_framework import serializers
from e_reimbursement.employees.models import Employee


class EmployeeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ("name", "bank_account_number")
