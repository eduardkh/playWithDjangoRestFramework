from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Paradigm, Language, Programmer
from .serializers import ParadigmSerializer, LanguageSerializer, ProgrammerSerializer

# Create your views here.


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer
    # individual per-view permissions
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    # individual per-view permissions
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
    # individual per-view permissions
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
