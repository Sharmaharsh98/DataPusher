from rest_framework import serializers
from .models import Destination_model

class DestinationSerializers(serializers.ModelSerializer):

    class Meta:
        model = Destination_model
        fields = ['title', 'content', 'created_by']