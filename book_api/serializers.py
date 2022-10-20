from dataclasses import Field, field, fields
from pyexpat import model
from rest_framework  import serializers
from .models import Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books

        fields = '__all__'