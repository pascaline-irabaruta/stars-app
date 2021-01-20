from django import forms
from .models import Project, Profile, Review
from tinymce.widgets import TinyMCE
from pyuploadcare.dj.forms import ImageField

SCORES = [
    (1,1),(2,2),
    (3,3),(4,4),
    (5,5),(6,6),
    (7,7),(8,8),
    (9,9),(10,10),
]
class ProjectForm(forms.ModelForm):
    project_pic = ImageField(label='')
    class Meta:
        model = Project
        fields = ("title", "description", "project_pic", "live_site",)
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control mb-4"}),
            "description":TinyMCE(attrs={'cols': 116, 'rows': 15}),
            "live_site":forms.URLInput(attrs={"class":"form-control mb-4"}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment", "design_score", "usability_score", "content_score",)
        widgets = {
            "comment":forms.Textarea(attrs={"class":"form-control mb-4"}),
            "design_score":forms.Select(choices=SCORES, attrs={"class":"form-control mb-4"}),
            "usability_score":forms.Select(choices=SCORES, attrs={"class":"form-control mb-4"}),
            "content_score":forms.Select(choices=SCORES, attrs={"class":"form-control mb-4"}),
        }

class UpdateProfileForm(forms.ModelForm):
    profile_pic = ImageField(label='')
    class Meta:
        model = Profile
        fields = ("bio", "profile_pic")
        widgets = {
            "bio":forms.Textarea(attrs={"class":"form-control mb-4", "value":"user.profile.bio"}),
        }
