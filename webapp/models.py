from django.db import models
from django.contrib.auth import User


class Contributer(models.Model):
  
    user = models.OneToOneField(User)

    # Addition info
    contact = models.CharField(max_length=12, blank=True)
    picture = models.ImageField(upload_to='profile_image', blank=True)

    def __unicode__(self):
        return self.user.username

class Reviewer(models.Model):
  
    user = models.OneToOneField(User)

    # Addition info
    contact = models.CharField(max_length=12, blank=True)
    picture = models.ImageField(upload_to='profile_image', blank=True)

    def __unicode__(self):
        return self.user.username

class standard_9_mathematics(models.Models):


    """class:9 subject: Mathematcis """
    topic_name = models.CharField(max_length=200, unique=True)
    pdf_doc = models.FileField(upload_to='docs', blank=True)
    video_doc = models.FileField(upload_to='docs', blank=True)
    url = models.URLField(blank=True)
    date_upload = models.DateField(auto_now=True)
    contributer = models.ForeignKey(AakashCentre) 
    download_count = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    approve = models.BooleanField(default=False)

    def __unicode__(self):
        return self.topic_name        

    def increment_download_count(self):
        self.download_count += 1
        self.save()


class standard_9_physics(models.Models):


    """class:9 subject: Physics """
    topic_name = models.CharField(max_length=200, unique=True)
    pdf_doc = models.FileField(upload_to='docs', blank=True)
    video_doc = models.FileField(upload_to='docs', blank=True)
    url = models.URLField(blank=True)
    date_upload = models.DateField(auto_now=True)
    contributer = models.ForeignKey(AakashCentre) 
    download_count = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    approve = models.BooleanField(default=False)

    def __unicode__(self):
        return self.topic_name        

    def increment_download_count(self):
        self.download_count += 1
        self.save()



class standard_9_chemistry(models.Models):


    """class:9 subject: chemistry """
    topic_name = models.CharField(max_length=200, unique=True)
    pdf_doc = models.FileField(upload_to='docs', blank=True)
    video_doc = models.FileField(upload_to='docs', blank=True)
    url = models.URLField(blank=True)
    date_upload = models.DateField(auto_now=True)
    contributer = models.ForeignKey(AakashCentre) 
    download_count = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    approve = models.BooleanField(default=False)

    def __unicode__(self):
        return self.topic_name        

    def increment_download_count(self):
        self.download_count += 1
        self.save()


class standard_10_mathematics(models.Models):


    """class:10 subject: Mathematcis """
    topic_name = models.CharField(max_length=200, unique=True)
    pdf_doc = models.FileField(upload_to='docs', blank=True)
    video_doc = models.FileField(upload_to='docs', blank=True)
    url = models.URLField(blank=True)
    date_upload = models.DateField(auto_now=True)
    contributer = models.ForeignKey(AakashCentre) 
    download_count = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    approve = models.BooleanField(default=False)

    def __unicode__(self):
        return self.topic_name        

    def increment_download_count(self):
        self.download_count += 1
        self.save()



class standard_10_physics(models.Models):


    """class:9 subject: physics """
    topic_name = models.CharField(max_length=200, unique=True)
    pdf_doc = models.FileField(upload_to='docs', blank=True)
    video_doc = models.FileField(upload_to='docs', blank=True)
    url = models.URLField(blank=True)
    date_upload = models.DateField(auto_now=True)
    contributer = models.ForeignKey(AakashCentre) 
    download_count = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    approve = models.BooleanField(default=False)

    def __unicode__(self):
        return self.topic_name        

    def increment_download_count(self):
        self.download_count += 1
        self.save()

class standard_10_chemistry(models.Models):


    """class:9 subject: chemistry """
    topic_name = models.CharField(max_length=200, unique=True)
    pdf_doc = models.FileField(upload_to='docs', blank=True)
    video_doc = models.FileField(upload_to='docs', blank=True)
    url = models.URLField(blank=True)
    date_upload = models.DateField(auto_now=True)
    contributer = models.ForeignKey(AakashCentre) 
    download_count = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    approve = models.BooleanField(default=False)

    def __unicode__(self):
        return self.topic_name        

    def increment_download_count(self):
        self.download_count += 1
        self.save()




class Contact(models.Model):
    """ Contacts """
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    message = models.TextField(max_length=500)

    def __unicode__(self):
        return self.email

class Faq(models.Model):
    """FAQs"""
    question = models.TextField(max_length=500)
    answer = models.TextField(max_length=1000)

    def __unicode__(self):
        return self.question
