from django.db import models

#import basic user model; it's a built-in model that we can use in user models.
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    #this way we are using built User model fields; the User built-in fields are Username, email, firstname, lastname;
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # add additional attributes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
