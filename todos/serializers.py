from dataclasses import fields
from rest_framework import serializers

from .models import Todo

class ToDoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            "id",
            "title",
            "body",
        )