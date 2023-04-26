from django.contrib import admin
from .models import Buy, ChatGlobal, ChatOnly, Comentariya, Product, Account
# Register your models here.
admin.site.register([Buy, ChatGlobal, ChatOnly, Comentariya, Product, Account])