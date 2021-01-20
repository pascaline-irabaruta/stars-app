from django.test import TestCase
from .models import Profile, Project, Review
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTest(TestCase):

    def setUp(self):
        self.new_user = User(username="pascy", email="pascy@gmail.com",
                             password="pascy12345")
        self.new_user.save()
        self.new_profile = Profile(user=self.new_user, bio="Hey there!")
        self.new_profile.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_profile(self):
        self.new_profile.save()
        users = User.objects.all()
        self.assertTrue(len(users)>0)

class ProjectTest(TestCase):

    def setUp(self):
        self.new_user = User(username="pascy", email="pascy@gmail.com",
                             password="pascy12345")
        self.new_user.save()
        self.new_profile = Profile(user=self.new_user, bio="hey there!")
        self.new_profile.save()
        self.new_project = Project(author=self.new_user, title=" Title",
                                   description=" description", live_site="gmail.com")
        self.new_project.save()


    def test_instance(self):
        self.assertTrue(isinstance(self.new_project, Project))

    def test_save_project(self):
        self.new_project.save()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_search_project(self):
        self.new_project.save()
        searched_project = Project.search_projects("Title")
        self.assertTrue(len(searched_project)==1)
