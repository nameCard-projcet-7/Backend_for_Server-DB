from rest_framework import serializers
from .models import Namecard, PostImage

class NamecardSerializers(serializers.ModelSerializer):
	class Meta:
		model = Namecard
		fields = ('Company','Name','Role','PhoneNumber','Address','Email')

class PostSerializer(serializers.ModelSerializer):
	img = serializers.ImageField(use_url=True)
	class Meta:
		model = PostImage
		fields = ('title','contents','img')

