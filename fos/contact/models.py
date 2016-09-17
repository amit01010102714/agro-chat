from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Contact(models.Model):
    Name= models.CharField(max_length=100)
    Email = models.EmailField()
    Subject = models.CharField(max_length=150)
    Message = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
    	return self.Name

    def __str__(self):
    	return self.Name

    def get_absolute_url(self):
    	return reverse("contact", kwargs={})
