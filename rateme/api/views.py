from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer
from ..models import Profile, Projects
from rest_framework import viewsets

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProjectView(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
