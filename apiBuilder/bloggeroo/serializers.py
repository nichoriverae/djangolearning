from django.contrib.auth.models import User, Group
from .models import List, Card
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('name')

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card 
        fields = ('title', 'description', 'story_points', 'business_value')