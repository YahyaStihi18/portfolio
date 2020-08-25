from django.db import models

class Contact(models.Model):
    name = models.CharField('Name',max_length=200)
    phone = models.BigIntegerField()
    email = models.EmailField()
    text = models.TextField()
    def __str__(self):
        return self.name



class Work(models.Model):
    name = models.CharField(max_length=200)
    youtube_code = models.CharField(max_length=200)
    info = models.TextField()
    rating = models.CharField(max_length=5)
    client = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    time = models.IntegerField()
    p1 = models.TextField()
    p2 = models.TextField()
    p3 = models.TextField()
    def __str__(self):
        return self.name

class Offer(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.CharField(max_length=900)
    def __str__(self):
        return self.title

class Comment(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    comment = models.TextField()
    def __str__(self):
        return self.name




