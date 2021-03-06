from django.core.urlresolvers import reverse 
from django.db import models

# Create your models here.

class Stock(models.Model):
    title = models.CharField(max_length=120)
    faina = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    oua  = models.IntegerField(default=0)
    lapte = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    ciocolata = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    frisca = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    
    def __unicode__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    sales_price = models.DecimalField(decimal_places=2, max_digits=100,\
                                                null=True, blank=True)
    #image = models.FileField(upload_to='products/images', null=True)

    # product_type = { 1 - tort, 2 - prajiitura}
    product_type  = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

        
    faina = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)
    oua  = models.IntegerField(default=0)
    lapte = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)
    ciocolata = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)
    frisca = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)


    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'slug')

    def get_price(self):
        return self.price

    def get_absolute_url(self):
        return reverse("single_product", kwargs={"slug": self.slug})


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='products/images/')
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.product.title


class VariationManager(models.Manager):

    def all(self):
        return super(VariationManager, self).filter(active=True)
    def sizes(self):
        return self.all().filter(category='size')

    def colors(self):
        return self.all().filter(category='color')    


VAR_CATEGORIES = (
    ('size', 'size'),
    ('color', 'color'),
    ('package', 'package'),
)
class Variation(models.Model):
    product = models.ForeignKey(Product)
    category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='size')
    title = models.CharField(max_length=120)
    image = models.ForeignKey(ProductImage, null=True, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = VariationManager()

    def __unicode__(self):
        return self.title
    



