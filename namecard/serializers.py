from rest_framework import serializers
from .models import Namecard

class NamecardSerializers(serializers.ModelSerializer):
	class Meta:
		model = Namecard
		fields = ('company','name','role','phonenumber','address','email')