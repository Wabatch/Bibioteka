from django.conf.urls import include
from django.db import router
from rest_framework import routers
from django.urls import path, re_path

from api.views import BookViewset, UsersViewset

router = routers.DefaultRouter()
router.register('books', BookViewset, 'books')
router.register('users', UsersViewset, 'users')

urlpatterns = [
    re_path(r'^', include(router.urls))
]