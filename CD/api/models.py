from django.db import models
from django.contrib.auth.models import User

# Minecraft Server Models


class Location(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()


class Jail(models.Model):
    name = models.TextField()
    location_min = models.OneToOneField(Location, on_delete=models.CASCADE, related_name='location_min')
    location_max = models.OneToOneField(Location, on_delete=models.CASCADE, related_name='location_max')
    is_max_security = models.BooleanField(default=False)
    slave_spawn = models.OneToOneField(Location, on_delete=models.CASCADE, related_name='slave_spawn')


class Town(models.Model):
    name = models.TextField()
    description = models.TextField()
    major = models.OneToOneField('Player', on_delete=models.CASCADE, related_name='major')


class Player(models.Model):
    uuid = models.TextField(primary_key=True)
    town = models.ForeignKey(Town, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_soldier = models.BooleanField(default=False)
    jail = models.ForeignKey(Jail, on_delete=models.CASCADE, null=True)


class Slave(models.Model):
    slave_timer = models.IntegerField()
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    owner = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='owner')
    jail = models.ForeignKey(Jail, on_delete=models.CASCADE, null=True)


class CriminalRecord(models.Model):
    date = models.DateTimeField()
    message = models.TextField()
    player = models.OneToOneField(Player, on_delete=models.CASCADE)

# Wiki Models


class Section(models.Model):
    name = models.TextField()


class Page(models.Model):
    class TypeChoices(models.IntegerChoices):
        PLUGIN = 1
        GUIDE = 2
        TOWN = 3
    title = models.TextField()
    body = models.TextField()
    type = models.IntegerField(choices=TypeChoices.choices)
    related_pages = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
