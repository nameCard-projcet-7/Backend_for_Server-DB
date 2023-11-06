from django.urls import path, include
from .views import *

urlpatterns = [
	path("getinform/",getinform),
	path("gener/", generate_inform),
]