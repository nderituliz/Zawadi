from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from pyuploadcare.dj.models import ImageField

class Profile(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_photo = ImageField(manual_crop='500x500')
    bio = models.TextField(default="Here is my bio...")
    contact = models.CharField(max_length=30)

    def __str__(self):
        return self.username.username

def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except Exception as error:
            print(error)
post_save.connect(post_save_user_model_receiver,sender=settings.AUTH_USER_MODEL)

class Projects(models.Model):
    title = models.CharField(User, max_length=200)
    image = ImageField(manual_crop='1920x1080')
    image2 = ImageField(null=True, manual_crop='1920x1080')
    description = models.TextField(max_length=200)
    url = models.URLField(null=True, blank=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="images")

    @classmethod
    def get_all_projects(cls):
        projects = Projects.objects.all()
        return projects

    @classmethod
    def get_post(cls, id):
        projects = Projects.objects.filter(user=id)
        return projects

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

class Categories(models.Model):
    name = models.ManyToManyField(Projects)
