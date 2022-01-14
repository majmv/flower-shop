from django.db import models

from django.conf import settings
# Create your models here.


class User(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return str(self.id) 
