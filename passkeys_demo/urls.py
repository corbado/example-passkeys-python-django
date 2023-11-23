from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path('<path:unknown_path>/', lambda request, unknown_path: redirect('/'), name='fallback')
]