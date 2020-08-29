from django.db import models

from tenant_users.tenants.models import UserProfile


class User(UserProfile):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
