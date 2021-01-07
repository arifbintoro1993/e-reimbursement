from django.db import models
from django.utils.translation import gettext_lazy as _

from django_multitenant.models import TenantModel
from model_utils.models import TimeStampedModel


class Employee(TenantModel, TimeStampedModel):
    name = models.CharField(_("Employee Name"), blank=True, max_length=255)
    bank_account_number = models.CharField(_("Employee Name"), blank=True, max_length=255)

    tenant_id = "id"

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.name
