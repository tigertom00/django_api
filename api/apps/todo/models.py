from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Todo(models.Model):
    """Model definition for Todo."""
    user = models.ForeignKey(User, related_name="todos", on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=64)
    day = models.DateField(null=True, blank=True)
    reminder = models.BooleanField(default=False)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Todo."""

        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        """Unicode representation of Todo."""
        return self.text
