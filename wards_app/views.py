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

class ProjectList(ListView):
    model = Project
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.filter(publish_date__lte=timezone.now()).order_by("-publish_date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_user"] = self.request.user
        return context
class ProjectDetail(DetailView):
    model = Project
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_user"] = self.request.user
        return context

class ProjectCreate(LoginRequiredMixin, CreateView):
    login_url = "/accounts/login/"
    redirect_field_name = "premios_app/project_detail.html"
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_user"] = self.request.user
        return context

class ProjectUpdate(LoginRequiredMixin ,UpdateView):
    login_url = "/accounts/login/"
    redirect_field_name = "premios_app/project_detail.html"
    model = Project
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_user"] = self.request.user
        return context

class ProjectDelete(LoginRequiredMixin, DeleteView):
    login_url = "/accounts/login/"
    redirect_field_name = "premios_app/project_detail.html"
    model = Project
    success_url = reverse_lazy("project_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_user"] = self.request.user
        return context

class UserDetail(LoginRequiredMixin, DetailView):
    login_url = "/accounts/login/"
    redirect_field_name = "premios_app/user_detail.html"
    model = User
    template_name = "premios_app/user_detail.html"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_user"] = self.request.user
        return context

@login_required
def update_profile(request, pk):
    profile = User.objects.get(pk=pk)
    current_user = request.user

    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            updated_profile = form.save(commit=False)
            updated_profile.user = current_user
            updated_profile.save()
            return redirect("user_detail", pk=profile.pk)
    else:
        form = UpdateProfileForm()
    return render(request, "premios_app/user_profile_form.html", context={"form":form,"current_user":current_user,"profile":profile})

@login_required
def review_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    current_user = request.user

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project
            review.author = current_user
            review.save()
            return redirect("project_detail", pk=project.pk)
    else:
        form = ReviewForm()
    return render(request, "premios_app/review_form.html", context={"form":form,"project":project})

@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    project_pk = review.project.pk
    review.delete()
    return redirect("project_detail", pk=project_pk)
