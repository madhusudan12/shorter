from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import CASCADE


class Member(models.Model):
    user=models.OneToOneField(User,on_delete=CASCADE)
    location=models.CharField(max_length=50)
    description=models.CharField(max_length=256)
    profile_image=models.ImageField(upload_to="profile_images",blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    author=models.ForeignKey(Member,on_delete=CASCADE)
    title=models.CharField(max_length=256)
    description=models.TextField()
    image=models.ImageField(upload_to="post_images",blank=True)
    time=models.DateTimeField()


    def __str__(self):
        return self.title

class Clap(models.Model):
    author=models.ForeignKey(Member,on_delete=CASCADE)
    post=models.ForeignKey(Post,on_delete=CASCADE)

    def __str__(self):
        return self.author.user.username+"clapped"

class Comment(models.Model):
    author=models.ForeignKey(Member,on_delete=CASCADE)
    post=models.ForeignKey(Post,on_delete=CASCADE)

    def __str__(self):
        return "commented on "+self.post.description+" by "+self.author.user.username

