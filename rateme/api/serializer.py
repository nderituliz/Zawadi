from rest_framework import serializers
from rest_framework.views import APIView
from rateme.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id' 'username', 'profile_photo', 'bio', 'contact')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'title', 'image', 'description', 'url', 'user',)
