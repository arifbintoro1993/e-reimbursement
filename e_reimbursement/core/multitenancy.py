from django.conf import settings
from django.core.cache import cache
from django_multitenant.utils import set_current_tenant, get_current_tenant


class SetCurrentTenantFromUser(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def get_employee(self, request):
        employee_key = "user-{}-employee".format(request.user.pk)
        employee = cache.get(employee_key)

        if not employee:
            employee = request.user.employee
            cache.set(employee_key, request.user.employee)

        return employee

    def __call__(self, request):

        if request.path.strip("/").split("/")[0] == settings.ADMIN_URL.strip("^/"):
            set_current_tenant(None)
        else:
            if request.user.is_authenticated:
                employee = self.get_employee(request)
                set_current_tenant(employee)
            else:
                set_current_tenant(None)
            request.current_tenant = get_current_tenant()

        response = self.get_response(request)
        set_current_tenant(None)
        return response
