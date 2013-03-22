from django.db import models
# Create your models here.

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone

class UserManager(BaseUserManager):
  def create_user(self, email=None, password=None, **extra_fields):
    """
    Creates and saves a User with the given email and password.
    """
    now = timezone.now()
    if not email:
        raise ValueError('Please enter your email address.')
    
    email = UserManager.normalize_email(email)
    
    user = self.model(email=email)

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, password):
    u = self.create_user(email, password)
    u.is_admin = True
    u.save(using=self._db)
    return u

class User(AbstractBaseUser):
  email = models.EmailField(max_length=254, unique=True, db_index=True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  
  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = [] # other than USERNAME_FIELD and password, I think 

  def get_full_name(self):
    return self.email

  def get_short_name(self):
    return self.email # for now

  def is_staff(self):
    return self.is_admin

  def __unicode__(self):
    return self.email

  def has_perm(self, perm, obj=None):
    return True # is this what I want?

  def has_module_perms(self, app_label):
    return True # is this what I want?

class Post(models.Model): # what's this for?
  user = User
  post = models.TextField()