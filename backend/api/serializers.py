from rest_framework import serializers
from .models import Opinion

class OpinionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    data = serializers.DateField()
    name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)