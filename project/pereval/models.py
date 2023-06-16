from django.db import models


class User(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True)
    fam = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    otc = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)

class Coords(models.Model):
    latitude = models.CharField(blank=True, null=True)
    longitude = models.CharField(blank=True, null=True)
    height = models.CharField(blank=True, null=True)

class Level (models.Model):
    winter = models.TextField(blank=True, null=True)
    spring = models.TextField(blank=True, null=True)
    summer = models.TextField(blank=True, null=True)
    autumn = models.TextField(blank=True, null=True)

class Pereval(models.Model):
    STATUS_COORDS = [
        ('new', 'new'),
        ('pending', 'pending'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected'),
    ]

    status = models.CharField(max_length=12, choices=STATUS_COORDS,default='new')
    beauty_title = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    other_title = models.TextField(blank=True, null=True)
    connect = models.TextField(blank=True, null=True)
    add_time = models.TimeField(auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)


class Image(models.Model):
    pereval = models.ForeignKey(Pereval, related_name='images', on_delete=models.CASCADE)
    title = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data = models.CharField(max_length=320)