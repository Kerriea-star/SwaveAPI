from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, age, password=None):
        if not email:
            raise ValueError("You must have an email address!")
        if not username:
            raise ValueError("You must have username!")
        if not password:
            raise ValueError("You must have password!")
        

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            age = age,
        )

        user.set_passoward(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, age, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
            age=age,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=30)
    bio = models.TextField(blank=True, null=True, max_length=2000)
    age = models.DateField(default=date.today())
    birth_place = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30, blank=True, null=True)
    what_are_you_seeking_on_site = models.CharField(max_length=30, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='image', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'email', 'password', 'first_name', 'last_name', 'age')

    objects = MyAccountManager()


    def __str__(self):
        return self.username + "," + self.email
    
    def has_perms(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True