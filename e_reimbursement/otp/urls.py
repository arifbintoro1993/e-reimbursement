from django.urls import path

from e_reimbursement.otp.api.views import OTPVerifyView, ResendOTPView

app_name = "otp"
urlpatterns = [
    path("verify/", OTPVerifyView.as_view(), name="verify"),
    path("resend-otp/", ResendOTPView.as_view(), name="resend_otp"),
]
