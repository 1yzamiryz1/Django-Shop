from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import reverse_lazy

from . import views

app_name = 'accounts'

urlpatterns = [
	path('login/', views.LoginView.as_view(), name='login'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
	path("signup/", views.SignupView.as_view(), name="signup"),
	path(
			"password_reset/",
			auth_views.PasswordResetView.as_view(success_url=reverse_lazy("accounts:password_reset_done")),
			name="password_reset"
			),
	path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path(
			"reset/<uidb64>/<token>/",
			auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy("accounts:password_reset_complete")),
			name="password_reset_confirm"
			),
	path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
	]
