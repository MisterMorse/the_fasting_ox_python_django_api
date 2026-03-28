from django.urls import path

from prayers import views

urlpatterns = [
    path("", views.prayer_list),
]
