from django.db import models
from django.conf import settings


class Comment(models.Model):
    content = models.TextField()
    time = models.DateTimeField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    time = models.DateTimeField()
    comments = models.ManyToManyField(Comment, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.author.username+"@"+str(self.time)