from django.urls import path

from backend.views import user_views as views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
]

