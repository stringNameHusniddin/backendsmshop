from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.utils import timezone

now = timezone.now()

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, is_biznes, password=None):
		user = self.model(
			email=self.normalize_email(email),
			username=username,
            is_biznes=is_biznes
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, is_biznes, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
            is_biznes=is_biznes
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='images/users/')

    is_biznes = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'is_biznes']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
	
class Product(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/product/', null=True, )
    body = models.TextField()
    cost = models.IntegerField()
    like = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=now,)

    def __str__(self):
        return self.title

class Comentariya(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=now)
    userImage = models.TextField(null=True)

    def __str__(self):
        return self.title



class ChatGlobal(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.TextField()
    userImage = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class ChatOnly(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    friend = models.IntegerField()
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    userImage = models.TextField(null=True)

    def __str__(self):
        return self.title

class Buy(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    max_num = models.IntegerField()



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

