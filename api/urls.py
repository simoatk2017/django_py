# basic URL Configurations
from django.urls import include, path
#from django.conf.urls import url, include
# import routers
from rest_framework import routers

# import everything from views
from .views import *
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')
# define the router
router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)
# specify URL Path for rest_framework
urlpatterns = [
    #path(r'^docs/', include('api.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path(r'^$', schema_view),
    path('hello/', HelloView.as_view(), name='hello'),

]
#urlpatterns += router.urls