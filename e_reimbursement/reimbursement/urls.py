from django.urls import path

from e_reimbursement.reimbursement.views import ReimbursementListView

app_name = "reimbursements"
urlpatterns = [
    path("", ReimbursementListView.as_view(), name="list"),
]
