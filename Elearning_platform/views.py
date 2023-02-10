from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


# ---------Pagination Class
class Paginate(PageNumberPagination):
    page_size = 2


# ---------List models. It returns the list of objects using "list()" and "queryset".
class ListModel(ListModelMixin, GenericAPIView):
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = Paginate

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = User.objects.all()
        else:
            # user = self.request.user
            queryset = User.objects.filter(first_name='Aalian')
        return queryset


# -------- Create models
class CreateModel(CreateModelMixin, GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# -------- List and Create models (BOTH)
class ListCreateModel(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'url'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# -------- Retrieve model. It returns only one object using "get_object()" based on "lookup_field".
class RetrieveModel(RetrieveModelMixin, GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = ['first_name', 'last_name']

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # -----overriding object function for multiple_look_up fields
    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        for field in self.lookup_field:
            filter[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter)
        return obj


# -------- Update model. updating object using "lookup_field". Using "put()" method to update.
class UpdateModel(UpdateModelMixin, GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# class DestroyModel(DestroyModelMixin, GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'id'
#
#     def destroy(self, request, pk ,  *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def perform_destroy(self, instance):
#         instance.delete()

