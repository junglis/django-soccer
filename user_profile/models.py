from django.db import models
from django.conf import settings

# Create your models here.
class Team(models.Model):
    User = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True)
    team_name = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.team_name

class Player(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    def get_full_name(self):
        full_name = self.first_name+' '+self.last_name
        full_name.strip()
        return full_name

    def __unicode__(self):
        return self.get_full_name()