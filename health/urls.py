from django.urls import path

from health import views

urlpatterns = [
    path("deployment/", views.health_deployment),
    path("database/", views.health_database),
]
