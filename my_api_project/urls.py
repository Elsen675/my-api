from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken import views
from graphene_django.views import GraphQLView
from django.views.generic import RedirectView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="My Movie API",
      default_version='v1',
      description="Part II - Movie API with Documentation",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   
)

urlpatterns = [
    path('', RedirectView.as_view(url='swagger/', permanent=False)),
    
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path("graphql/", GraphQLView.as_view(graphiql=True)),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api-token-auth/', views.obtain_auth_token),
]