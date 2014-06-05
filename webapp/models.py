from django.db import models
from django.contrib.auth.models import User


class Contributor(models.Model):
    """Contributor."""
    user = models.OneToOneField(User)

    # Addition info
    contact = models.CharField(max_length=12, blank=True)
    picture = models.ImageField(upload_to='contributor_profile_image', blank=True)

    def __unicode__(self):
        return self.user.username


class Reviewer(models.Model):
    """Reviewer."""
    user = models.OneToOneField(User)

    # Addition info
    contact = models.CharField(max_length=12, blank=True)
    picture = models.ImageField(upload_to='reviewer_profile_image', blank=True)

    def __unicode__(self):
        return self.user.username


class Class(models.Model):
    """This will be class number like first, second .. eight .. tenth."""
    class_number = models.IntegerField(default=1)
    remark = models.TextField()

    def __unicode__(self):
        return u"%d" % (self.class_number)


class Subject(models.Model):
    """Subjects."""
    name = models.CharField(max_length=200, unique=True)
    class_number = models.ForeignKey(Class)
    pdf = models.FileField(upload_to='docs', blank=True)
    video = models.FileField(upload_to='videos', blank=True)
    url = models.URLField(blank=True)
    uploaded_on = models.DateField(auto_now=True)
    contributor = models.ForeignKey(Contributor) 
    download_count = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    approve = models.BooleanField(default=False)


    def __unicode__(self):
        return self.name


    def increment_download_count(self):
        self.download_count += 1
        self.save()

    
    def increment_rating(self):
        self.rating += 1
        self.save()

        
class Contact(models.Model):
    """Contact us."""
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    message = models.TextField(max_length=500)


    def __unicode__(self):
        return u"%s - %s" % (self.name, self.email)


class Faq(models.Model):
    """FAQs"""
    question = models.TextField(max_length=500)
    answer = models.TextField() #


    def __unicode__(self):
        return self.question
