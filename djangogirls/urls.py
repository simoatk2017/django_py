"""djangogirls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')
from rest_framework_simplejwt import views as jwt_views

from api import views  as test_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('formreg/', include('formApp.urls')),
    path('testtt', include('smartnotes.urls')),
    path('contact/', include('contact.urls')),

    path('hello/', test_view.HelloView.as_view(), name='hello'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('api/', include('api.urls')),
    path('doc/', schema_view),
    path('filter_app/', include('filter_app.urls'), name='filter_and_pagination'),
    path('about/', include('about.urls')),
    path('sender/', include('contactApp.urls'))
    #path('logout/', auth_views.LogoutView.as_view(
        #template_name='registration/logged_out.html',next_page=None),name = 'logout')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Blogs && Projects Dashboard"
admin.site.site_title = "Blogs  Admin Dashboard "
admin.site.site_index_title = "Welcome To projects Admin Panel"