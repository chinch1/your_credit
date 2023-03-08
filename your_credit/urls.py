"""your_credit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import path, include

# For API views
from bank.api.router import router_banks
from client.api.router import router_clients
from credit.api.router import router_credits

schema_view = get_schema_view(
    openapi.Info(
        title="Your Credit API",
        default_version='v1',
        description="API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="nicolaandresr@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # API routes
    path('api/', include((router_clients.urls))),
    path('api/', include((router_banks.urls))),
    path('api/', include((router_credits.urls))),

    # UI routes
    path('client/', include('client.urls')),
    path('bank/', include('bank.urls')),
    path('credit/', include('credit.urls')),

    # Swagger
    path('docs/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),
]
