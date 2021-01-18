from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Q
from star_ratings.models import Rating
from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField
import statistics

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField(blank=True)
    profile_pic = ImageField(blank=True, manual_crop="")

    def save_profile(self):
        self.save()

    def get_user_projects(self):
        return self.projects.all

    def __str__(self):
        return self.user.username
