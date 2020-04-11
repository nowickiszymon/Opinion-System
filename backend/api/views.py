from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Opinion
from .serializers import OpinionSerializer

class OpinionList(APIView):
        def get(self, request, format=None):
                snippet = Opinion.objects.all()
                serializer = OpinionSerializer(snippet, many=True)
                return Response(serializer.data)
