from django.urls import path
from zipairline import views


urlpatterns = [
    path('airplanes/', views.AirplaneList.as_view()),
    path('airplanes/<int:pk>', views.AirplaneDetail.as_view()),
]
