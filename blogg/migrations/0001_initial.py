# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comment'
        db.create_table(u'blogg_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user.UserProfile'])),
        ))
        db.send_create_signal(u'blogg', ['Comment'])

        # Adding model 'Post'
        db.create_table(u'blogg_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user.UserProfile'])),
        ))
        db.send_create_signal(u'blogg', ['Post'])

        # Adding M2M table for field comments on 'Post'
        m2m_table_name = db.shorten_name(u'blogg_post_comments')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'blogg.post'], null=False)),
            ('comment', models.ForeignKey(orm[u'blogg.comment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'comment_id'])


    def backwards(self, orm):
        # Deleting model 'Comment'
        db.delete_table(u'blogg_comment')

        # Deleting model 'Post'
        db.delete_table(u'blogg_post')

        # Removing M2M table for field comments on 'Post'
        db.delete_table(db.shorten_name(u'blogg_post_comments'))


    models = {
        u'blogg.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['user.UserProfile']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'blogg.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['user.UserProfile']"}),
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blogg.Comment']", 'symmetrical': 'False'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
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

    complete_apps = ['blogg']