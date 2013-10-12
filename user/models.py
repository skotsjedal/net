from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#from django.db.models.signals import post_save
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
            email=MyUserManager.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        u = self.create_user(
            username,
            email,
            password=password,
            date_of_birth=date_of_birth
        )

        u.is_admin = True
        u.save(using=self._db)
        return u


class UserProfile(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'date_of_birth']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def __str__(self):
        return "%s's profile" % self.user


        #def create_user_profile(sender, instance, created, **kwargs):
        #    if created:
        #       profile, created = UserProfile.objects.get_or_create(user=instance)
        #
        #post_save.connect(create_user_profile, sender=User)