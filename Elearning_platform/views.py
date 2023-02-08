from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class UserViewSet(APIView):
    def get(self, request):
        obj = User.objects.all()
        dic = {}
        name = []
        f_name = []
        l_name = []
        for user in obj:
            name.append(user.username)
            f_name.append(user.first_name)
            l_name.append(user.last_name)

        dic['name'] = name
        dic['first_name'] = f_name
        dic['last_name'] = l_name
        return Response(dic)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        context = {'request': request}
        import pdb
        pdb.set_trace()
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
