from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)


class Menu(models.Model):
    title = models.CharField(max_length=200)
    items = models.ManyToManyField(MenuItem)


