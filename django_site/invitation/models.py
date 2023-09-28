from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    code = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.title


# class InvitationPage(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     code = models.CharField(max_length=6)

# InvitationPage.objects.create_table()