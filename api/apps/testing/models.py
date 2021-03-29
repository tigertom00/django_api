from django.db import models

# Create your models here.


class Post(models.Model):
    """Model definition for Post."""
    title = models.CharField(max_length=64, blank=True)
    text = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return self.title
