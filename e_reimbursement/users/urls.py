from django.urls import path

from e_reimbursement.users.views import (
    user_detail_view,
    user_redirect_view,
)
from e_reimbursement.users.views import UserListView

app_name = "users"
urlpatterns = [
    path("", UserListView.as_view(), name="list"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
