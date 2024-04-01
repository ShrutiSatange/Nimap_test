# serializers.py

from rest_framework import serializers
from .models import Client, Project

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by']

class ProjectSerializer(serializers.ModelSerializer):
    client_name = serializers.ReadOnlyField(source='client.client_name')
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'client_name', 'users', 'created_at', 'created_by']