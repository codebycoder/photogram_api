from .models import User


def get_user(**kwargs):
    return User.objects.get(**kwargs)
