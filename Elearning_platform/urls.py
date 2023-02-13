from django.urls import path

from .views import ListView, RetrieveView, UpdateView, DestroyView, ListCreate, RetrieveUpdate, RetrieveDestroy, \
    RetrieveDestroyUpdate

urlpatterns = [
    path('', ListView.as_view(), name='user-detail'),
    path('list-create/', ListCreate.as_view()),
    path('update/<int:pk>', UpdateView.as_view()),
    path('destroy/<int:pk>', DestroyView.as_view()),
    path('retrieve/<int:pk>/', RetrieveView.as_view()),
    path('retrieve-update/<int:pk>', RetrieveUpdate.as_view()),
    path('retrieve-destroy/<int:pk>', RetrieveDestroy.as_view()),
    path('retrieve-destroy-update/<int:pk>', RetrieveDestroyUpdate.as_view()),

]
