from django.urls import path
from .views import DetailsView, DetailsApiView

urlpatterns = [
    path('', DetailsView.as_view()),
    path('details/<pk>', DetailsApiView.as_view()),
]