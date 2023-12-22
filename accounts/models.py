from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass
    # # https://chat.openai.com/c/a070ab40-05d9-4631-ba62-094ce0d7c92b
    # groups = models.ManyToManyField(Group, related_name='custom_class_users_groups')
    # user_permissions = models.ManyToManyField(Permission, related_name='custom_class_users_permissions')

    def __str__(self):
        return self.username
