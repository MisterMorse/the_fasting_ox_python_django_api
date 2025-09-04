from django.urls import path

from events import views

urlpatterns = [
    path('', views.event_list),
    path('<int:pk>', views.event_detail )
]
