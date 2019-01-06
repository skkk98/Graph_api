from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer
from django.views.generic import TemplateView, View
from django.views.decorators.csrf import csrf_exempt
from requests import request as r1
import json
# Create your views here.
def hi(request):
    return HttpResponse('hi')

class Page(TemplateView):
    template_name = 'index.html'

class Pageinfo(TemplateView):
    template_name = 'page-info.html'

@csrf_exempt
def post_data(request):
	if request.method=="POST":
		try:
			pageAccesstoken=request.POST.get("pageAccessToken",'')
			pageID=request.POST.get("pageID",'')
			header="OAuth "+pageAccesstoken
			fieldProperty=request.POST.get("fieldProperty",'')
			fieldPropertyValue=request.POST.get("fieldPropertyValue",'')
			print(fieldProperty,fieldPropertyValue)
			data={}
			data[fieldProperty]=fieldPropertyValue
			# print(data)
			response1=r1('POST',"https://graph.facebook.com/"+pageID,data=data,headers={"Authorization": header})
			response=json.dumps(response1.json())
			return HttpResponse(response)
		except:
			return HttpResponse("failure")
	return HttpResponse("invalid")

class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
