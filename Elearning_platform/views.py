from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, ListCreateAPIView \
    , RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class MyPaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


# -------- ListApiView using concrete classes. Implements just get method. use list() function.
class ListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Add pagination
        paginator = MyPaginator()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


# -------- RetrieveApiView using concrete classes. override get_queryset() to filter through query_params.
class RetrieveView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        queryset = User.objects.get(id=user_id)
        return User.objects.filter(id=user_id)
        # return queryset


# -------- UpdateVIew using concrete classes. override get_queryset() to filter through query_params.
class UpdateView(UpdateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        queryset = get_object_or_404(User, id=user_id)
        if queryset is not None:
            return User.objects.filter(id=queryset.id)
        else:
            return Response('Not found')


# -------- DestroyView using concrete classes. override get_queryset() to filter through query_params.
class DestroyView(DestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        queryset = get_object_or_404(User, id=user_id)
        return User.objects.filter(id=queryset.id)


# -------- ListCreateAPIView combination of List and Create.
class ListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# -------- RetrieveUpdateAPIView combination of Retrieve and Create.Provide get(), Put(), Patch() methods.
class RetrieveUpdate(RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        queryset = User.objects.get(id=user_id)
        return User.objects.filter(id=user_id)


# -------- RetrieveDestroyAPIView.Provide get() and delete() methods.
class RetrieveDestroy(RetrieveDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        queryset = User.objects.get(id=user_id)
        return User.objects.filter(id=user_id)


# -------- RetrieveUpdateDestroyAPIView.Provide get(), put(), patch() and delete() methods.

class RetrieveDestroyUpdate(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    # queryset = User.objects.all()

    def get_queryset(self):
        user_id = self.kwargs['pk']
        queryset = User.objects.get(id=user_id)
        return User.objects.filter(id=user_id)
