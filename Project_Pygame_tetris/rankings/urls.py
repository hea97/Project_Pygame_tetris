from django.urls import path
from .views import PlayerListCreate, PlayerDetail

urlpatterns = [
    path('players/', PlayerListCreate.as_View(), name='player-list-create'),
    path('players/<int:pk>/', PlayerDetail.as_view(), name='player-detail'),
]