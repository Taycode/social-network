from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from rest_framework.authtoken.models import Token


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_picture')
    followers = models.ManyToManyField(User, related_name='+')
    following = models.ManyToManyField(User, related_name='+')


def create_user_profile(sender, **kwargs):
    if sender:
        if kwargs['created']:
            UserProfile.objects.create(user=kwargs['instance'])
            Token.objects.create(user=kwargs['instance'])


post_save.connect(create_user_profile, User)
