from django.db import models
from django.contrib.auth.models import User

import datetime

class Tag(models.Model):
    text = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.text;

class Address(models.Model):
    street  = models.CharField(max_length=200)
    city    = models.CharField(max_length=200)
    state   = models.CharField(max_length=200)
    zip     = models.CharField(max_length=200)
    long    = models.CharField(max_length=200)
    lat     = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.street + " " + self.city + " " + self.state;

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    address = models.OneToOneField(Address)
    tags = models.ManyToManyField(Tag)
    rating = models.IntegerField();

    def __unicode__(self):
        return self.name

class Property(models.Model):
    user        = models.ForeignKey(User)
    address     = models.OneToOneField(Address)
    sqft        = models.IntegerField();
    numOfRooms  = models.IntegerField();
    numOfStairs = models.IntegerField();
    lawn_sqft   = models.IntegerField();

    type = models.CharField(max_length=200, choices=(
        ('house', 'House'),
        ('condo', 'Condo'),
    ))
    
    def __unicode__(self):
        return self.user.username + u" address";
        
class Project(models.Model):
    title   = models.CharField(max_length=200)
    members = models.ManyToManyField(User)
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title;

class Bid(models.Model):
    project = models.ForeignKey(Project)
    vendor  = models.ForeignKey(Vendor)
    description = models.TextField();
    
    def __unicode__(self):
        return self.vendor.name + u" bid for " + self.project.title;