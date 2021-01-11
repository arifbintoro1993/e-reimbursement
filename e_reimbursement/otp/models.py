from django.db import models

from django_otp.plugins.otp_email.models import EmailDevice
from model_utils.models import TimeStampedModel


class EmailDeviceExtra(TimeStampedModel):
    device = models.OneToOneField(EmailDevice, related_name="extra", on_delete=models.CASCADE)
    reimbursement = models.ForeignKey("reimbursement.Reimbursement", blank=True, null=True, on_delete=models.CASCADE)

    def verify_token_reimbursement(self, token, reimbursement):
        if self.reimbursement != reimbursement:
            return False
        else:
            return self.device.verify_token(token)
