from rest_framework import viewsets, permissions, generics
from rest_framework.pagination import PageNumberPagination
from .models import Movie
from .serializers import MovieSerializer, UserSerializer
from django.contrib.auth.models import User


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('id')
    serializer_class = MovieSerializer
    pagination_class = StandardResultsSetPagination


    def get_permissions(self):

        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]