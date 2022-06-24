from django.urls import path
from . import views

urlpatterns = [
    path('caprate/<str:area>/', views.caprate_list.as_view(), name="caprate"),
    path('cashoncash/<str:area>/', views.cashoncash_list.as_view(), name="cashoncash"),
]