from django.db import models
from django.contrib.auth.models import User
import random


class ConfirmationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)
    is_verified = models.BooleanField(default=False)

    @classmethod
    def create(cls, user):
        code = ''.join(random.choices('0123456789', k=6))
        confirmation_code = cls(user=user, code=code)
        confirmation_code.save()
        return confirmation_code

