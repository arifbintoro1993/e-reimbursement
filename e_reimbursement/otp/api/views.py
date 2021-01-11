from rest_framework import views, permissions
from rest_framework import status
from rest_framework.response import Response
from django_otp.plugins.otp_email.models import EmailDevice
from django_otp.util import random_number_token

from e_reimbursement.otp.models import EmailDeviceExtra
from e_reimbursement.reimbursement.models import Reimbursement


class OTPVerifyView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        token = request.POST.get("token")
        reimbursement_pk = request.POST.get("reimbursement_pk")
        reimbursement = Reimbursement.objects.get(pk=reimbursement_pk)
        device_extra = EmailDeviceExtra.objects.get(reimbursement=reimbursement)

        verified = device_extra.verify_token_reimbursement(token, reimbursement)
        if verified:
            reimbursement.status = Reimbursement.STATUS_CHOICES.accepted
            reimbursement.save()
            device_extra.device.confirmed = True
            device_extra.device.save()
            return Response(status=status.HTTP_200_OK, data={})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"token": "Invalid token."})


class ResendOTPView(views.APIView):

    def post(self, request, *args, **kwargs):
        token = random_number_token()
        device, created = EmailDevice.objects.get_or_create(
            user=request.user,
            email=request.user.email,
            confirmed=False,
            name="default",
            defaults={"token": token}
        )
        if device:
            device.generate_challenge()
        return Response(status=status.HTTP_200_OK, data={})
