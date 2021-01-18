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
