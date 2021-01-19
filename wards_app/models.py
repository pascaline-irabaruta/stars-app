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

class Project(models.Model):
    author = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
    title = models.CharField(max_length=144)
    description = HTMLField()
    project_pic = ImageField(manual_crop="")
    publish_date = models.DateTimeField(auto_now_add=True)
    live_site = models.URLField(max_length=256)

    def save_project(self):
        self.save()

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk":self.pk})

    @classmethod
    def search_projects(cls, search_term):
        return cls.objects.filter(Q(title__icontains = search_term)|Q(description__icontains = search_term)|Q(author__username=search_term))

    def __str__(self):
        return self.title

class Review(models.Model):
    project = models.ForeignKey(Project, related_name="reviews", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    comment = models.TextField()
    design_score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    usability_score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    content_score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    star_rating = GenericRelation(Rating, related_query_name='ratings')

    def save_review(self):
        self.save()
    def get_average_score(self):
        return round(statistics.mean([self.design_score, self.usability_score, self.content_score]),1)

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk":self.pk})

    def __str__(self):
        return self.comment
