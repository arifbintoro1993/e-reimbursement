from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.template.defaultfilters import slugify

from model_utils.models import TimeStampedModel
from model_utils import Choices
from djmoney.models.fields import MoneyField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

from e_reimbursement.core.models import EmployeeTenantModel


def get_upload_path(instance, filename):
    return "{}/products/{}".format(instance.employee.pk, filename)


class Reimbursement(EmployeeTenantModel, TimeStampedModel):
    CATEGORY_CHOICES = Choices(
        ("transport", _("Transport")),
        ("food_and_beverages", _("Food & Beverages")),
        ("office_supplies", _("Office Supplies")),
    )
    STATUS_CHOICES = Choices(
        ("submitted", _("Submitted")),
        ("on_progress", _("On Progress")),
        ("accepted", _("Accepted")),
        ("rejected", _("Rejected")),
    )
    date_of_purchase = models.DateField(
        _("Date of Purchase"), auto_now=False, auto_now_add=False
    )
    description = models.TextField(_("Description"))
    category = models.CharField(
        _("Category"),
        max_length=30,
        choices=CATEGORY_CHOICES,
        default=CATEGORY_CHOICES.transport,
        db_index=True,
    )
    amount = MoneyField(
        _("Amount"),
        max_digits=settings.HIGH_DECIMAL_MAX_DIGITS,
        decimal_places=settings.DECIMAL_PLACES,
        default_currency="IDR",
    )
    attachment = models.ImageField(
        upload_to=get_upload_path,
        blank=True,
        null=True,
        max_length=255,
    )
    status = models.CharField(
        _("Status"),
        max_length=30,
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES.submitted,
        db_index=True,
    )

    attachment_thumbnail = ImageSpecField(
        source="attachment",
        processors=[ResizeToFit(width=240, height=240, upscale=False)],
        format="JPEG",
        options={"quality": 60},
    )

    class Meta:
        verbose_name = _("Reimbursement")
        verbose_name_plural = _("Reimbursements")

    def __str__(self):
        return "Reimbursement: {}, {} - {}".format(
            self.date_of_purchase, self.category, self.amount
        )
