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
    adminId = models.ForeignKey(UserAccounts, on_delete=models.CASCADE, related_name='Artist', blank=False)
    artistName = models.CharField(unique=True,max_length=54, help_text='Eg: Abeke')
    description = models.CharField(max_length=1000, help_text='artist Description')
    artistPhoto = models.ImageField(upload_to='assets/', help_text='photo size details')
    slug = models.SlugField(default='', null=False)
    uploadDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.artistName

class All_Artist(models.Model):
    adminId = models.ForeignKey(UserAccounts, on_delete=models.CASCADE, related_name='uploads', blank=False)
    artistName = models.CharField(unique=True,max_length=54, help_text='Eg: freshers')
    artistPhoto = models.FileField(upload_to='photos/', help_text='photo size details')
    uploadDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.adminId.username}'s Photo {self.id}"
    
class Slide(models.Model):
    image = models.ImageField(upload_to='slides/')
    link = models.URLField()
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption


class Release(models.Model):
    artist_name = models.CharField(max_length=255)
    featured_artist = models.CharField(max_length=255)
    songwriters = models.CharField(max_length=255)
    producers = models.CharField(max_length=255)
    music_type = models.CharField(max_length=255)
    release_date = models.DateField()
    type = models.CharField(max_length=50, choices=[
        ('single', 'Single'),
        ('album', 'Album'),
        ('ep', 'EP')
    ])
    file_upload = models.FileField(upload_to='uploads/')
    cover_art = models.FileField(upload_to='uploads/')
    muamala = models.FileField(upload_to='uploads/')
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"Release by {self.artist_name} ({self.music_type})"


# class Release(models.Model):
#     ARTIST_NAME_MAX_LENGTH = 100
#     FEATURED_ARTIST_MAX_LENGTH = 200
#     SONG_WRITERS_MAX_LENGTH = 200
#     PRODUCERS_MAX_LENGTH = 200
#     MUSIC_TYPE_MAX_LENGTH = 200
#     PHONE_NUMBER_MAX_LENGTH = 15
#     EMAIL_MAX_LENGTH = 254

#     # Artist information
#     artist_name = models.CharField(max_length=ARTIST_NAME_MAX_LENGTH)
#     featured_artist = models.CharField(max_length=FEATURED_ARTIST_MAX_LENGTH)
#     songwriters = models.CharField(max_length=SONG_WRITERS_MAX_LENGTH)
#     producers = models.CharField(max_length=PRODUCERS_MAX_LENGTH)
#     music_type = models.CharField(max_length=MUSIC_TYPE_MAX_LENGTH)
#     release_date = models.DateField()

#     # Type of release (single, album, ep)
#     RADIO_CHOICES = [
#         ('single', 'Single'),
#         ('album', 'Album'),
#         ('ep', 'EP'),
#     ]
#     release_type = models.CharField(max_length=10, choices=RADIO_CHOICES)

#     # Files uploaded
#     file_upload = models.FileField(upload_to='uploads/')
#     cover_art = models.FileField(upload_to='cover_art/')
#     muamala = models.FileField(upload_to='muamala/')

#     # Contact information
#     phone_number = models.CharField(max_length=PHONE_NUMBER_MAX_LENGTH)
#     email = models.EmailField(max_length=EMAIL_MAX_LENGTH)

#     def __str__(self):
#         return f"Release by {self.artist_name} on {self.release_date}"
