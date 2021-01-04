from django.contrib import admin
# get from settings
from django.contrib.auth import get_user_model

from django.contrib.auth.admin import UserAdmin

# import from our forms
from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


# class to show form in admin site
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # for list display in admin site
    list_display = ['email', 'username', ]


admin.site.register(CustomUser, CustomUserAdmin)