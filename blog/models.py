from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=30)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=False,auto_now=True)
    user=models.CharField(max_length=20,null=True)
    email=models.EmailField(null=True)
    like=models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    comment=models.TextField()
    commenter=models.CharField(max_length=20)
    email=models.EmailField(null=True)
    date=models.DateTimeField(auto_now_add=False,auto_now=True)
    post=models.ForeignKey(Post)

    def __unicode__(self):
        return self.comment

class SignUp(models.Model):
    first_name=models.CharField(max_length=100,blank=True,null=True)
    last_name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(null=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)

    def __unicode__(self):
        return self.email
