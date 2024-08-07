from accounts.forms import AuthenticationForm
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages
from .forms import SignupForm
from .models import User


class LoginView(auth_views.LoginView):
	template_name = "accounts/login.html"
	form_class = AuthenticationForm
	redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
	pass


class SignupView(CreateView):
	model = User
	form_class = SignupForm
	template_name = 'accounts/signup.html'
	success_url = reverse_lazy('accounts:login')

	def form_valid(self, form):
		user = form.save(commit=False)
		user.save()
		return super().form_valid(form)

	def form_invalid(self, form):
		for field, error_list in form.errors.items():
			for error in error_list:
				messages.error(self.request, f"{field}: {error}")

		return super().form_invalid(form)