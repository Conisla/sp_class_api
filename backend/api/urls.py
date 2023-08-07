from django.urls import path
from . import views

urlpatterns = [
    path('predict', views.PredictImage, name="predict")
]
