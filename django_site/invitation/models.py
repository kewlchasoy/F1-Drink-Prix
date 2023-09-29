from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    code = models.CharField(max_length=6, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_pages', default=None, null=True)
    user_list = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accessed_pages', default=None, null=True)

    def __str__(self):
        return self.title