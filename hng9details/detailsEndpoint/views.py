from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import DetailsSerializer
from .models import Details

# Create your views here.
class DetailsView(ListAPIView):
    queryset = Details.objects.all()
    serializer_class= DetailsSerializer
