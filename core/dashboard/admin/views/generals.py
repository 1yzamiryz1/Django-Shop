from dashboard.permissions import HasAdminAccessPermission
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class AdminDashboardHomeView(LoginRequiredMixin, HasAdminAccessPermission, TemplateView):
	template_name = 'dashboard/admin/home.html'
