from django.db import models

class News(models.Model):
    title=models.CharField(max_length=200)
    writer=models.CharField(max_length=100)
    date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to="news/",blank=True,null=True)

    def __str__(self):
        return self.title

    def summary(self): 
        return self.body[:60]

class Mreviews(models.Model):
    medicine=models.CharField(max_length=100)
    image=models.ImageField(upload_to="mreview/",blank=True,null=True)
    nickname=models.CharField(max_length=100)
    date=models.DateTimeField()
    body=models.TextField()

    def __str__(self):
        return self.medicine

    def summary(self): 
        return self.body[:60]

class Hreviews(models.Model):
    hospital=models.CharField(max_length=100)
    image=models.ImageField(upload_to="hreview/",blank=True,null=True)
    nickname=models.CharField(max_length=100)
    date=models.DateTimeField()
    body=models.TextField()

    def __str__(self):
        return self.hospital

    def summary(self): 
        return self.body[:60]