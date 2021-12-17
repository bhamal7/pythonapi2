from django.shortcuts import render
from .models import Hero
from rest_framework.views import APIView
from .serilizer import HeroSerializer

from django.http import JsonResponse

# Create your views here.
class HeroView(APIView):
    serializer_class = HeroSerializer

    def get(self,request,*args,**kwrgs):
        data = Hero.objects.all()
        serialie_data= HeroSerializer(data,many = True)
        return JsonResponse(serialie_data.data, safe = False)

    def post(self,request,*args,**kwrgs):
        #print(request.GET)
        tname = request.GET['tname']
        data = Hero.objects.all().filter(age__range=[13,19])
        print(data)
        serialie_data= HeroSerializer(data,many = True)
        return JsonResponse(serialie_data.data, safe = False)

