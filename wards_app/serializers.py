from rest_framework import serializers
from .models import Project, Review
from django.contrib.auth.models import User


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "comment", "design_score", "usability_score",
                  "content_score",)
