from django.urls import path
from . import views

urlpatterns = [
    path('caprate/', views.caprate_list.as_view(), name="caprate"),
    path('caprate/<str:area>/', views.caprate_list.as_view(), name="caprate"),
    path('cashoncash/', views.cashoncash_list.as_view(), name="cashoncash"),
    path('cashoncash/<str:area>/', views.cashoncash_list.as_view(), name="cashoncash"),
]