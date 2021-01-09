import re
from django.conf import settings
from django.urls.resolvers import get_resolver
from django.urls.exceptions import Resolver404
from django.utils.deprecation import MiddlewareMixin

from braces.views import LoginRequiredMixin


class IsAuthenticatedMiddleware(MiddlewareMixin):
    def __init__(self, *args, **kwargs):
        self.non_auth_url_name = getattr(settings, "NON_AUTH_URL_NAME", [])
        super(IsAuthenticatedMiddleware, self).__init__(*args, **kwargs)

    def is_non_auth_view(self, view_name):
        matching_results = [
            re.search(pattern, view_name) for pattern in self.non_auth_url_name
        ]

        return any(matching_results)

    def process_request(self, request):
        try:
            resolver_match = get_resolver().resolve(request.path)

            if not request.user.is_authenticated and not self.is_non_auth_view(
                resolver_match.view_name
            ):
                response = LoginRequiredMixin().no_permissions_fail(request)
                return response
        except Resolver404:
            pass
