from rest_framework import generics
from django.shortcuts import render
from drf.models import Women
from drf.serializers import WomenSerializer

def index(request):
    context={

    }
    return render(request, "drf/index.html", context)

class WomenAPIView(generics.ListAPIView):
    queryset=Women.objects.all()
    serializer_class=WomenSerializer

