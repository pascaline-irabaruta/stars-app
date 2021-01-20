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
