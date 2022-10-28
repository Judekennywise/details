from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import DetailsSerializer
from .models import Details

# Create your views here.
class DetailsView(ListAPIView):
    queryset = Details.objects.all()
    serializer_class= DetailsSerializer

class DetailsApiView(RetrieveAPIView):
    serializer_class = DetailsSerializer
    queryset = Details.objects.all()
