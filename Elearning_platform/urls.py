from django.urls import path

from .views import UserView

urlpatterns = [
    path('', UserView.as_view({'get': 'list', 'post': 'create'}), name='user-detail'),
    path('update/<int:pk>/', UserView.as_view({'get': 'retrieve', 'put': 'update'}), name='user-detail')
    # path('list-create/', ListCreate.as_view()),
    # path('update/<int:pk>', UpdateView.as_view()),
    # path('destroy/<int:pk>', DestroyView.as_view()),
    # path('retrieve/<int:pk>/', RetrieveView.as_view()),
    # path('retrieve-update/<int:pk>', RetrieveUpdate.as_view()),
    # path('retrieve-destroy/<int:pk>', RetrieveDestroy.as_view()),
    # path('retrieve-destroy-update/<int:pk>', RetrieveDestroyUpdate.as_view()),

]
