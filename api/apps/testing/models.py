from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Post(models.Model):
    """Model definition for Post."""
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=64)
    day = models.DateField(null=True, blank=True)
    reminder = models.BooleanField(default=False)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return self.text
