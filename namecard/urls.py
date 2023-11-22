from django.urls import path, include
from .views import *

urlpatterns = [
	path("get&post/",namecardAPI.as_view()),
	path("ocr/",openCV_OCR_API.as_view()),
	path("postpic/",post_picture.as_view()),
]