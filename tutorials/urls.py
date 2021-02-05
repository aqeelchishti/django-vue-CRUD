from django.urls import path, include, re_path
from tutorials import views 

from rest_framework import routers
import rest_framework

router = routers.DefaultRouter()
router.register(r'tutorials', views.TutorialViewSet)


app_name = 'tutorials'
urlpatterns = [ 
    path('api/tutorials', views.tutorial_list),
    re_path('^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    path('api/tutorials/published', views.tutorial_list_published),
    path('api/', include(router.urls)),
    #path('api/', include('rest_framework.urls', namespace='rest_framework'))
]