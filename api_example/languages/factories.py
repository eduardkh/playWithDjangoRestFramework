import factory
from .models import Language


class LanguageFactory(factory.django.DjangoModelFactory):
    """
    Create a Language
    """
    class Meta:
        model = Language

    name = factory.Faker('first_name')



"""
https://pythonhosted.org/django-anonymizer/djangofaker.html


from shell.py

from languages.factories import LanguageFactory
languages = LanguageFactory.create_batch(10)
"""