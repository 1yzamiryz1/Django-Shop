from django.urls import path
from azbankgateways.urls import az_bank_gateways_urls
from . import views

app_name = "payment"

urlpatterns = [path('verify/', views.PaymentVerifyView.as_view(), name='verify'),
               path("bankgateways/", az_bank_gateways_urls()),
               ]
