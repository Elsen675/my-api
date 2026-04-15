from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, UserCreateView

router = DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('', include(router.urls)),
]