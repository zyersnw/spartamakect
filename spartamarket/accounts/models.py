from django.contrib.auth.models import User
from django.db import models


class Follow(models.Model):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='to_user_follow')
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='from_user_follow')

    class Meta:
        db_table = 'follow'
