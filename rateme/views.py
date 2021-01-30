from django.shortcuts import render
from urllib import request
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile, Projects, Categories
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .forms import ProfileForm, ProjectsForm
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
def home(request):
    word = "This is a house"
    current_user = request.user
    projects = Projects.get_all_projects()

    return render(request, 'pages/home.html', {"word": word, "projects": projects})
