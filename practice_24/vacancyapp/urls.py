from django.urls import path
from .views import *

urlpatterns = [
    path('', StartPageView.as_view(), name='start_page'),
    path('vacancy/<int:pk>/', DetailPageView.as_view(), name='vacancy'),
]
