from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView,CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Project, Review
from django.contrib.auth.models import User
from .forms import ProjectForm, ReviewForm, UpdateProfileForm
from django.utils import timezone
from django.urls import reverse_lazy
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProjectSerializer, UserSerializer

# Create your views here.
