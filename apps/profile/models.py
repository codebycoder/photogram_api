from django.db import models

# Create your models here.

GenderChoices = (
    ('Male', 'MALE'),
    ('Female', 'FEMALE')
)


class UserProfile(models.Model):
    user = models.ForeignKey('apps_user.User', on_delete=models.CASCADE, related_name='profile', db_index=True)
    bio = models.TextField(blank=True)
    gender = models.CharField(max_length=10, choices=GenderChoices, default=None, blank=True, null=True)
    links = models.CharField(max_length=120, blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    class Meta:
        ordering = ('-created_at',)
