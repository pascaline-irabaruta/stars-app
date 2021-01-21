from rest_framework import serializers
from .models import Project, Review
from django.contrib.auth.models import User

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "comment", "design_score", "usability_score",
                  "content_score",)

class ProjectSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ("id", "author", "title", "description", "publish_date",
                  "project_pic", "live_site", "reviews",) # to add author and reviews
class UserSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ("id", "username", "email", "projects")
