from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.urls import reverse
from django.utils.crypto import get_random_string

from django_multitenant.models import TenantManager

from e_reimbursement.core.models import EmployeeTenantModel
from e_reimbursement.users.tasks import send_email_created_user_info


class UserManager(BaseUserManager, TenantManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def create_employee(self, email=None, password=None, count=0, **extra_fields):
        email = self.normalize_email(email)
        count = "{0:0=4d}".format(count + 1)
        username = "{}{}".format("employee", count)
        user = self.model(username=username, email=email, **extra_fields)
        password_temp = get_random_string(length=6)
        user.set_password(password_temp)
        user.save(using=self._db)

        send_email_created_user_info.delay(
            username,
            password_temp,
            email,
        )
        return user


class User(EmployeeTenantModel, AbstractUser):
    objects = UserManager()

    class Meta:
        unique_together = ("id", "employee")

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
