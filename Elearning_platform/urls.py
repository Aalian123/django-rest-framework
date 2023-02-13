from django.urls import path

from .views import ListModel, CreateModel, ListCreateModel, RetrieveModel, UpdateModel, DestroyModel

urlpatterns = [
    path('', ListModel.as_view(), name='user-detail'),
    path('create/', CreateModel.as_view()),
    path('list-create/', ListCreateModel.as_view()),
    path('update/<int:id>', UpdateModel.as_view()),
    path('destroy/<int:id>', DestroyModel.as_view()),
    path('retrieve/<str:first_name>/<str:last_name>/', RetrieveModel.as_view()),
]
