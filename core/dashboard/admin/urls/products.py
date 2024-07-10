from dashboard.admin import views
from django.urls import path


urlpatterns = [
	path('product/list/', views.AdminProductListView.as_view(), name='product-list'),
	path('product/create/', views.AdminProductCreateView.as_view(), name='product-create'),
	path('product/<int:pk>/edit/', views.AdminProductEditView.as_view(), name='product-edit'),
	path('product/<int:pk>/delete/', views.AdminProductDeleteView.as_view(), name='product-delete'),
	]
