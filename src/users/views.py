from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from src.users.models import User, Person
from src.users.serializers import CreateUserSerializer, UserSerializer, PersonSerializer


class UserCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Creates user accounts
    """

    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class HealthCheckViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        return Response({"status": "healthy"})