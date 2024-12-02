from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

class UserManager(BaseUserManager):
  def create_user(self,email,password=None):
    if not email:
      raise ValueError('User must have an email address')
    user = self.model(email=self.normalize_email(email))
    user.set_password(password)
    user.save(using=self._db)
    return user
  def create_superuser(self,email,password):
    user = self.create_user(email,password=password)
    user.is_superuser = True
    user.is_staff = True
    user.save(using=self._db)
    return user
class User(AbstractUser):
  email = models.EmailField(unique=True,max_length=255)
  username = models.CharField(max_length=255,unique=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  object = UserManager()

