# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stock'
        db.create_table(u'products_stock', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('faina', self.gf('django.db.models.fields.DecimalField')(default=29.99, max_digits=100, decimal_places=2)),
            ('oua', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('lapte', self.gf('django.db.models.fields.DecimalField')(default=29.99, max_digits=100, decimal_places=2)),
            ('ciocolata', self.gf('django.db.models.fields.DecimalField')(default=29.99, max_digits=100, decimal_places=2)),
            ('frisca', self.gf('django.db.models.fields.DecimalField')(default=29.99, max_digits=100, decimal_places=2)),
        ))
        db.send_create_signal(u'products', ['Stock'])

        # Adding field 'Product.faina'
        db.add_column(u'products_product', 'faina',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=100, decimal_places=2),
                      keep_default=False)

        # Adding field 'Product.oua'
        db.add_column(u'products_product', 'oua',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Product.lapte'
        db.add_column(u'products_product', 'lapte',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=100, decimal_places=2),
                      keep_default=False)

        # Adding field 'Product.ciocolata'
        db.add_column(u'products_product', 'ciocolata',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=100, decimal_places=2),
                      keep_default=False)

        # Adding field 'Product.frisca'
        db.add_column(u'products_product', 'frisca',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=100, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Stock'
        db.delete_table(u'products_stock')

        # Deleting field 'Product.faina'
        db.delete_column(u'products_product', 'faina')

        # Deleting field 'Product.oua'
        db.delete_column(u'products_product', 'oua')

        # Deleting field 'Product.lapte'
        db.delete_column(u'products_product', 'lapte')

        # Deleting field 'Product.ciocolata'
        db.delete_column(u'products_product', 'ciocolata')

        # Deleting field 'Product.frisca'
        db.delete_column(u'products_product', 'frisca')


    models = {
        u'products.product': {
            'Meta': {'unique_together': "(('title', 'slug'),)", 'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ciocolata': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '100', 'decimal_places': '2'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'faina': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '100', 'decimal_places': '2'}),
            'frisca': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '100', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lapte': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '100', 'decimal_places': '2'}),
            'oua': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '29.99', 'max_digits': '100', 'decimal_places': '2'}),
            'product_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sales_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '100', 'decimal_places': '2', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'products.productimage': {
            'Meta': {'object_name': 'ProductImage'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"}),
            'thumbnail': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'products.stock': {
            'Meta': {'object_name': 'Stock'},
            'ciocolata': ('django.db.models.fields.DecimalField', [], {'default': '29.99', 'max_digits': '100', 'decimal_places': '2'}),
            'faina': ('django.db.models.fields.DecimalField', [], {'default': '29.99', 'max_digits': '100', 'decimal_places': '2'}),
            'frisca': ('django.db.models.fields.DecimalField', [], {'default': '29.99', 'max_digits': '100', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lapte': ('django.db.models.fields.DecimalField', [], {'default': '29.99', 'max_digits': '100', 'decimal_places': '2'}),
            'oua': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'products.variation': {
            'Meta': {'object_name': 'Variation'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'default': "'size'", 'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.ProductImage']", 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '100', 'decimal_places': '2', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['products']