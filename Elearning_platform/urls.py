from django.urls import path
from rest_framework import routers

from .views import UserView, LoginView, LogoutView

router = routers.DefaultRouter()
router.register(r'users', UserView, basename='user')

urlpatterns = [
                  path('login/', LoginView.as_view(), name='login'),
                  path('logout/', LogoutView.as_view(), name='logout'),
                  # path('login/', obtain_auth_token, name='login'),

              ] + router.urls
