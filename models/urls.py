from django.urls import path
from .views import BikeModelListCreate, BikeModelRetrieveUpdateDestroy

urlpatterns = [
    path('', BikeModelListCreate.as_view(), name='maker-list-create'),
    path('model/<int:pk>/', BikeModelRetrieveUpdateDestroy.as_view(), name='maker-detail'),
]
