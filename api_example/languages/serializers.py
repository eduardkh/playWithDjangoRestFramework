from rest_framework import serializers
from .models import Paradigm, Language, Programmer


# class LanguageSerializer(serializers.ModelSerializer):
class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        # fields = ('id', 'name')
        fields = ('id', 'url', 'name')

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        # fields = ('id', 'name', 'paradigm')
        fields = ('id', 'url', 'name', 'paradigm')

class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        # fields = ('id', 'name')
        fields = ('id', 'url', 'name', 'languages')