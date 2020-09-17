from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    label = models.TextField(max_length=30)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

    def __str__(self):
        return f'{self.label} (x: {self.x}, y: {self.y}, z: {self.z})'


class Jail(models.Model):
    name = models.TextField()
    location_min = models.OneToOneField(Location, on_delete=models.CASCADE,
                                        related_name='location_min')
    location_max = models.OneToOneField(Location, on_delete=models.CASCADE,
                                        related_name='location_max')
    is_max_security = models.BooleanField(default=False)
    slave_spawn = models.OneToOneField(Location, on_delete=models.CASCADE,
                                       related_name='slave_spawn')

    def __str__(self):
        return self.name


class Town(models.Model):
    name = models.TextField()
    description = models.TextField()
    location = models.OneToOneField(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Player(models.Model):
    uuid = models.TextField(primary_key=True)
    town = models.ForeignKey(Town, on_delete=models.CASCADE, blank=True,
                             null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,
                                null=True)
    jail = models.ForeignKey(Jail, on_delete=models.CASCADE, blank=True,
                             null=True)
    is_soldier = models.BooleanField(default=False)
    is_major = models.BooleanField(default=False)

    def __str__(self):
        return self.uuid


class Slave(models.Model):
    slave_timer = models.IntegerField()
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    owner = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True,
                              null=True, related_name='owner')
    jail = models.ForeignKey(Jail, on_delete=models.CASCADE, blank=True,
                             null=True)

    def __str__(self):
        return self.player.uuid


class CriminalRecord(models.Model):
    date = models.DateTimeField()
    message = models.TextField()
    player = models.OneToOneField(Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.player.uuid


class Section(models.Model):
    name = models.TextField(max_length=30)

    def __str__(self):
        return self.name


class Page(models.Model):
    class TypeChoices(models.IntegerChoices):
        PLUGIN = 1
        GUIDE = 2
        TOWN = 3
    title = models.TextField()
    body = models.TextField()
    type = models.IntegerField(choices=TypeChoices.choices)
    related_pages = models.ForeignKey('self', on_delete=models.CASCADE,
                                      blank=True, null=True)
    section = models.OneToOneField(Section, on_delete=models.CASCADE)
    town = models.OneToOneField(Town,  on_delete=models.CASCADE, blank=True,
                                null=True)

    def __str__(self):
        return self.title
