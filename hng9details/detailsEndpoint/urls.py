from django.urls import path
from .views import DetailsView

urlpatterns = [
    path('', DetailsView.as_view()),
]