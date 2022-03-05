from rest_framework import viewsets
from rest_framework.response import Response
from users.models import User
from users.publisher import publish
from users.serializers import UserSerializer

class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer =  UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('user_created', serializer.data)
        return Response(serializer.data, status=201)
    
    def list(self, request):
        users =  User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response('User with id: {} not found'.format(pk), status=404)
    
