from django.db import models

class Contact(models.Model):
    name = models.CharField('Name',max_length=200)
    phone = models.BigIntegerField(max_length=13)
    email = models.EmailField()
    text = models.TextField()
    def __str__(self):
        return self.name

