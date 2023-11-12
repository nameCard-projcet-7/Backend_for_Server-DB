from rest_framework import serializers
from .models import Namecard

class NamecardSerializers(serializers.ModelSerializer):
	class Meta:
		model = Namecard
		fields = ('Company','Name','Role','PhoneNumber','Address','Email')
