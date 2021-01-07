from django.contrib.auth import get_user_model
from rest_framework import serializers

from e_reimbursement.employees.models import Employee

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    employee__name = serializers.CharField(source='employee.name')
    employee__bank_account_number = serializers.CharField(source='employee.bank_account_number')

    class Meta:
        model = User
        fields = ("email", "employee__name", "employee__bank_account_number", "url")

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }

    def create(self, validated_data):
        email = validated_data.pop("email")
        employee_data = validated_data.pop('employee')
        employee = Employee.objects.create(**employee_data)
        count = User.objects.count()
        user = User.objects.create_employee(email=email, employee=employee, count=count)
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.pop("email")
        instance.save()
        employee_data = validated_data.pop('employee')
        employee = instance.employee
        employee.name = employee_data["name"]
        employee.bank_account_number = employee_data["bank_account_number"]
        employee.save()
        return instance
