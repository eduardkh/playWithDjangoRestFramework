from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Language
from .serializers import LanguageSerializer

# Create your views here.


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )