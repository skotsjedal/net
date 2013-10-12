from django.contrib import admin
from blogg.models import *

class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('comments',)


admin.site.register(Comment)
admin.site.register(Post, PostAdmin)