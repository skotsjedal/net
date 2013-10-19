from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Comment(models.Model):
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey('Post')

    class Meta:
        verbose_name = u"Comment"
        verbose_name_plural = u"Comments"
        ordering = ['-time', ]

    def __unicode__(self):
        return self.author.username + "." + str(self.post.id) + "@" + str(self.time.strftime("%Y.%m.%d"))

    def get_absolute_url(self):
        return reverse('blog', kwargs={'pk': self.post.pk})


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    public = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('blog', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.title + "@" + str(self.time.strftime("%Y.%m.%d"))