
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

class User(AbstractUser):
    """"
    Login User
    各ユーザーPointを取得する
    """
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=150,
        unique=False,
        validators = [username_validator],
        help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
                    ),
    )
    email = models.EmailField(blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    point = models.ForeignKey(
        'Point',
        related_name='used_point_log',
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        default_permissions = ()