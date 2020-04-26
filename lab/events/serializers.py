from rest_framework import serializers

from events.models import Event
from babies.serializers import BabieSerializer

class EventSerializer(serializers.ModelSerializer):


    class Meta:
        model = Event
        fields = (
            'id',
            'eventName',
            'eventType',
            'description',
            'eventDate',
            'eventsToBaby'
        )