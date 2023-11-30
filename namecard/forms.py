# forms.py
from django import forms
class PostForm(forms.Form):
	img = forms.ImageField(error_messages={'required' : '사진을 첨부하라'},label=img)
