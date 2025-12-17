from django.urls import path

from events import views

urlpatterns = [
    path("", views.event_list),
    path("<str:category>/", views.event_list_by_category),
]
