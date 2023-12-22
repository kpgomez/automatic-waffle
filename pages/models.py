from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_users_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users_permissions')

    def __str__(self):
        return self.email # from wsvincent repo
