from django.urls import path

from .views import UserViewSet

urlpatterns = [
    path('', UserViewSet.as_view()),
]
