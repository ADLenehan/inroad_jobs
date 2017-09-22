from datetime import datetime
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None):

        return self._create_user(username, email, password)

    def create_superuser(self, username, email, password, **extra_fields):

        user = self._create_user(username, email, password, **extra_fields)
        user.is_active      = True
        user.is_superuser   = True
        user.is_staff       = True
        user.is_admin       = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    company = models.ForeignKey('jobs.Company', null=True, blank=True)
    company_email = models.EmailField(verbose_name='company email', max_length=255, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    role = models.CharField(max_length=200, null=True, blank=True, default='')
    start_date = models.DateField(blank=False, default=datetime.now)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=datetime.now)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_email(self):
        return self.email