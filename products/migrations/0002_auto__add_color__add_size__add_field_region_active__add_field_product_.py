# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Color'
        db.create_table(u'products_color', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'products', ['Color'])

        # Adding model 'Size'
        db.create_table(u'products_size', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'products', ['Size'])

        # Adding field 'Region.active'
        db.add_column(u'products_region', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Product.properties'
        db.add_column(u'products_product', 'properties',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.producer'
        db.add_column(u'products_product', 'producer',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field color on 'Product'
        db.create_table(u'products_product_color', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'products.product'], null=False)),
            ('color', models.ForeignKey(orm[u'products.color'], null=False))
        ))
        db.create_unique(u'products_product_color', ['product_id', 'color_id'])

        # Adding M2M table for field size on 'Product'
        db.create_table(u'products_product_size', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'products.product'], null=False)),
            ('size', models.ForeignKey(orm[u'products.size'], null=False))
        ))
        db.create_unique(u'products_product_size', ['product_id', 'size_id'])


    def backwards(self, orm):
        # Deleting model 'Color'
        db.delete_table(u'products_color')

        # Deleting model 'Size'
        db.delete_table(u'products_size')

        # Deleting field 'Region.active'
        db.delete_column(u'products_region', 'active')

        # Deleting field 'Product.properties'
        db.delete_column(u'products_product', 'properties')

        # Deleting field 'Product.producer'
        db.delete_column(u'products_product', 'producer')

        # Removing M2M table for field color on 'Product'
        db.delete_table('products_product_color')

        # Removing M2M table for field size on 'Product'
        db.delete_table('products_product_size')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'products.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['products.Category']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'products.color': {
            'Meta': {'ordering': "['name']", 'object_name': 'Color'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'products.images': {
            'Meta': {'ordering': "['sort']", 'object_name': 'Images'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'images'", 'null': 'True', 'to': u"orm['products.Product']"}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'products.product': {
            'Meta': {'ordering': "['sort', 'unit_price']", 'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'products'", 'null': 'True', 'to': u"orm['products.Category']"}),
            'color': ('django.db.models.fields.related.ManyToManyField', [], {'max_length': '255', 'to': u"orm['products.Color']", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_products.product_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'producer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'properties': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.related.ManyToManyField', [], {'max_length': '255', 'to': u"orm['products.Size']", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'trader': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': u"orm['products.Trader']"}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'})
        },
        u'products.region': {
            'Meta': {'ordering': "['sort', 'name']", 'object_name': 'Region'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'products.size': {
            'Meta': {'ordering': "['name']", 'object_name': 'Size'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'products.trader': {
            'Meta': {'ordering': "['sort', 'name']", 'object_name': 'Trader'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'traders'", 'to': u"orm['products.Region']"}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['products']