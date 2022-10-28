from django.urls import path
from .views import DetailsView,DetaislApiView

urlpatterns = [
    path('', DetailsView.as_view()),
    path('details/<pk>', DetaislApiView.as_view())
]