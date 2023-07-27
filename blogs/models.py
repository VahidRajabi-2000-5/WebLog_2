from django.db import models
from django.urls import reverse

from accounts.models import CustomUser

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    Status = models.BooleanField(default=True)
    
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    