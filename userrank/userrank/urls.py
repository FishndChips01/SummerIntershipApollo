from django.contrib import admin
from django.urls import path, include
from task.views import TweetModelViewSet , UserModelViewSet, create_comment
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tweets', TweetModelViewSet)
router.register(r'users', UserModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('comment/', create_comment, name='create_comment'),
]
