from django.db import models
# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager


class MyUserManager(BaseUserManager):
  def create_user(self, email):
    """
    Creates and saves a user with a given email and password.
    """
    now = timezone.now()
    if not email:
      raise ValueError('We need an email address so that we can contact you with information about the tournament.')
    if email:
       # make email domain lowercase
      username, domain = email.split('@')
      # username = username.lower() don't change username case
      domain = domain.lower() # domain is always case-insensitive
      email = str(username+"@"+domain)

    user = self.model(email=email)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self,email):
    user = self.create_user(email)
    user.is_admin = True
    user.save(using=self._db)

class MyUser(AbstractBaseUser):
  email = models.EmailField(max_length=254, unique=True, db_index=True)
  USERNAME_FIELD = 'email'
  #REQUIRED_FIELDS = ['']

  objects = MyUserManager()