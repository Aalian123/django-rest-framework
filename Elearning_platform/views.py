from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import User
from .serializers import UserSerializer


# --------Viewsets
class UserView(ViewSet):

    def list(self, request, pk=None):
        pk = pk
        if pk is not None:
            queryset = User.objects.get(pk=pk)
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data)

    def create(self, request):

        serializer = UserSerializer(data=request.data)
        import pdb
        pdb.set_trace()
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        instance = User.objects.get(id=pk)
        serializer = UserSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        instance = User.objects.get(id=pk)
        serializer = UserSerializer(instance)
        return Response(serializer.data)