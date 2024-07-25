from rest_framework import generics
from .models import Player
from .serializers import PlayerSerializer

class PlayerListCreate(generics.ListCreateAPIView):
    qeryest = Player.objects.all().order_dy('-score')
    serializer_class = PlayerSerializer

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryest = Player.objects.all()
    serializer_class = PlayerSerializer