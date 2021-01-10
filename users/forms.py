"""
we’ve imported CustomUser model via get_user_model
which looks to our AUTH_USER_MODEL config in settings.py.
This might feel a bit more circular than directly importing CustomUser here,
but it enforces the idea of making one single reference to the custom user model
rather than directly referring to it all over our project.
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)