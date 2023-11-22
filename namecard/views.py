from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import NamecardSerializers, PostSerializer
from .openCV_OCR import *
from rest_framework import status, generics
from rest_framework.views import APIView
from .models import Namecard, PostImage
from .forms import ImageUploadForm

class namecardAPI(APIView):
	def get(self, request):
		namecards = Namecard.objects.all()
		serializer = NamecardSerializers(namecards, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	def post(self, request):
		serializer = NamecardSerializers(data=request.data)
		if serializer.is_valid(): # 데이터 유효성 검사 해당 모델의 필드에 적합하면 True
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class openCV_OCR_API(APIView):
	def get(self, request):
		return JsonResponse(get_result(),json_dumps_params={'ensure_ascii':False})
class post_picture(APIView):
	def post(self, request):
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
