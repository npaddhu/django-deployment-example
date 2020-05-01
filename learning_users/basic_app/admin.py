from django.contrib import admin
from basic_app.models import UserProfileInfo
# Register your models here.

# We have to register the models in the admin, so that we can see our models once if we login admin
# Once we have edited this admin page, run migration
admin.site.register(UserProfileInfo)
