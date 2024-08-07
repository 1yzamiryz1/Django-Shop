from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['email'].label = 'Email'


class AuthenticationForm(auth_forms.AuthenticationForm):
	def confirm_login_allowed(self, user):
		super(AuthenticationForm, self).confirm_login_allowed(user)

# if not user.is_verified:
#     raise ValidationError("user is not verified")
