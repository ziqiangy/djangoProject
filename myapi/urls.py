from django.urls import include, path
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'words', views.WordViewSet)
router.register(r'notes', views.NoteViewSet)
router.register(r'wordsources', views.WordSourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]