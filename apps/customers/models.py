from django.db import models
from django_tenants.models import DomainMixin
from tenant_users.tenants.models import TenantBase


class Client(TenantBase):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    auto_create_schema = True


class Domain(DomainMixin):
    pass
