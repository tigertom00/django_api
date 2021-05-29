from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class MainStat(models.Model):
    """Model definition for MainStat."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stat = models.CharField(max_length=64)
    level = models.CharField(max_length=10, default='1')
    progress = models.IntegerField(default=1)

    class Meta:
        """Meta definition for MainStat."""

        verbose_name = 'MainStat'
        verbose_name_plural = 'MainStats'

    def __str__(self):
        """Unicode representation of MainStat."""
        return self.stat


class Character(models.Model):
    """Model definition for Character."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=64)
    level = models.CharField(max_length=10, default='1')
    progress = models.IntegerField(default=1)
    main_stats = models.ForeignKey(
        MainStat, on_delete=models.CASCADE, null=True, blank=True)

    # Character: Define fields here

    class Meta:
        """Meta definition for Character."""

        verbose_name = 'Character'
        verbose_name_plural = 'Characters'

    def __str__(self):
        """Unicode representation of Character."""
        return self.user
