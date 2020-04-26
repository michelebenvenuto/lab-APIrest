from rest_framework import serializers

from babies.models import Babie

class BabieSerializer(serializers.ModelSerializer):


    class Meta:
        model = Babie
        fields = (
            'firstName',
            'lastName'
        )