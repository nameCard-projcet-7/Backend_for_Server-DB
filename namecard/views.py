from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Namecard
from .serializers import NamecardSerializers
from .openCV_OCR import *
import json



@api_view(['GET'])
def generate_inform(reqeust):
	# api_view를 POST 형식으로 받아서 데이터 생성 어떻게 하는지 알아볼것
	json_data = test_for_makeing_json_from_dict()
	Namecard.objects.create(json_data)
	Namecard.save()
	return Response(Namecard.objects.all())

@api_view(['GET'])
def getinform(request):
	model = Namecard.objects.all()
	serializer = NamecardSerializers(model, many=True)
	return Response(serializer.data)