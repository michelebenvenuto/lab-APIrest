from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from babies.models import Babie
from babies.serializers import BabieSerializer

class BabieViewSet(viewsets.ModelViewSet):
    queryset = Babie.objects.all()
