from django.urls import path
from dashboard.admin import views
from dashboard.admin import views


urlpatterns = [path('home/', views.AdminDashboardHomeView.as_view(), name='home'),
               ]
