from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
import uuid
from django.utils.text import slugify
# Create your models here.


class UserAccounts(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_id = models.UUIDField(default=uuid.uuid4, unique=True)

# class Update(models.Model):
#     userId = models.ForeignKey(UserAccounts, on_delete=models.CASCADE, related_name='update', blank=False)
#     updateTitle = models.CharField(unique=True,max_length=54, help_text='Eg: freshers')
#     updateDescription = models.CharField(max_length=1000, help_text='update Description')
#     date = models.DateTimeField()
#     slug = models.SlugField(default='', null=False)

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.eventTitle)
#         super(Update, self).save(*args, **kwargs)

class Famous_Artist(models.Model):
    adminId = models.ForeignKey(UserAccounts, on_delete=models.CASCADE, related_name='events', blank=False)
    artistName = models.CharField(unique=True,max_length=54, help_text='Eg: freshers')
    description = models.CharField(max_length=1000, help_text='event Description')
    date = models.DateTimeField()
    artistPhoto = models.ImageField(upload_to='assets/', help_text='photo size details')
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return self.eventTitle
    

class All_Artist(models.Model):
    adminId = models.ForeignKey(UserAccounts, on_delete=models.CASCADE, related_name='uploads', blank=False)
    artistName = models.CharField(unique=True,max_length=54, help_text='Eg: freshers')
    artistPhoto = models.FileField(upload_to='photos/', help_text='photo size details')
    uploadDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.adminId.username}'s Photo {self.id}"