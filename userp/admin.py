from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['username', 'first_name',
                    'last_name', 'user_email']


admin.site.register(Profile, ProfileAdmin)
