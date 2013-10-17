# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Comment.post'
        db.add_column(u'blog_comment', 'post',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['blog.Post']),
                      keep_default=False)


        # Changing field 'Comment.time'
        db.alter_column(u'blog_comment', 'time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Removing M2M table for field comments on 'Post'
        db.delete_table(db.shorten_name(u'blog_post_comments'))


        # Changing field 'Post.time'
        db.alter_column(u'blog_post', 'time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    def backwards(self, orm):
        # Deleting field 'Comment.post'
        db.delete_column(u'blog_comment', 'post_id')


        # Changing field 'Comment.time'
        db.alter_column(u'blog_comment', 'time', self.gf('django.db.models.fields.DateTimeField')())
        # Adding M2M table for field comments on 'Post'
        m2m_table_name = db.shorten_name(u'blog_post_comments')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'blog.post'], null=False)),
            ('comment', models.ForeignKey(orm[u'blog.comment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'comment_id'])


        # Changing field 'Post.time'
        db.alter_column(u'blog_post', 'time', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'blog.comment': {
            'Meta': {'ordering': "['-time']", 'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['user.UserProfile']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Post']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['user.UserProfile']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'user.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['blog']