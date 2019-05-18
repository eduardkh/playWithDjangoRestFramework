from rest_framework import serializers
from .models import Language


# class LanguageSerializer(serializers.ModelSerializer):
class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        # fields = ('id', 'name', 'paradigm')
        fields = ('id', 'url', 'name', 'paradigm')