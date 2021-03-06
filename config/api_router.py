from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from e_reimbursement.users.api.views import UserViewSet
from e_reimbursement.reimbursement.api.views import ReimbursementViewSet
from e_reimbursement.otp.api.views import OTPVerifyView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("reimbursement", ReimbursementViewSet)

app_name = "api"
urlpatterns = router.urls
