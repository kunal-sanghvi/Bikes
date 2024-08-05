from django.urls import path
from .views import MakerListCreate, MakerRetrieveUpdateDestroy

urlpatterns = [
    path('', MakerListCreate.as_view(), name='maker-list-create'),
    path('<int:pk>/', MakerRetrieveUpdateDestroy.as_view(), name='maker-detail'),
]
