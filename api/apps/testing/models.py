from django.db import models

# Create your models here.


class Post(models.Model):
    """Model definition for Post."""
    text = models.CharField(max_length=64, blank=True)
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
