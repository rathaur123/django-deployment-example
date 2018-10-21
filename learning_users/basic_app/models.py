from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# to add additional attributes that generic User model does not have


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=False)

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(blank=True,upload_to='profile_pics')

    def __str__(self):
        # print out the default username attribute of the generic User
        return self.user.username

