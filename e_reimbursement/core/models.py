from django.db import models

from django_multitenant.fields import TenantForeignKey, TenantOneToOneField
from django_multitenant.models import TenantModel

from e_reimbursement.employees.models import Employee


class EmployeeForeignKey(TenantForeignKey):
    pass


class EmployeeOneToOneField(TenantOneToOneField):
    pass


class EmployeeTenantModel(TenantModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tenant_id = 'employee_id'

    class Meta:
        abstract = True
