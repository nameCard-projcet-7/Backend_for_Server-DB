from rest_framework import serializers
from .models import Namecard, Post

class NamecardSerializers(serializers.ModelSerializer):
	class Meta:
		model = Namecard
		fields = ('Company','Name','Role','PhoneNumber','Address','Email')

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		field = ('title','text', 'image')