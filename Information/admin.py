from django.contrib import admin
from Information.models import user

class userForm(admin.ModelAdmin):
    list_dis=("Name","Email","Department","Position")

admin.site.register(user,userForm)