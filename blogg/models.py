from django.db import models
from django.conf import settings
from datetime import datetime


class Comment(models.Model):
    content = models.TextField()
    time = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name = u"Comment"
        verbose_name_plural = u"Comments"
        ordering = ['-time', ]

    def __unicode__(self):
        return self.author.username + "@" + str(self.time)


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(Comment, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.title + "@" + str(self.time)