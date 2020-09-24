from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def max_world_size(value):
    if value > abs(30000000.0):
        raise ValidationError(
            'The value is greater than the Minecraft World Size Limit',
            params={'value': value}
        )


def max_world_height(value):
    if value < 0 or value > 255.0:
        raise ValidationError(
            'The value is not a valid Minecraft World Height',
            params={'value': value}
        )


class Location(models.Model):
    label = models.TextField(max_length=30)
    x = models.DecimalField(max_digits=23,
                            decimal_places=15,
                            validators=[max_world_size]
                            )
    y = models.DecimalField(max_digits=18,
                            decimal_places=15,
                            validators=[max_world_height]
                            )
    z = models.DecimalField(max_digits=23,
                            decimal_places=15,
                            validators=[max_world_size]
                            )

    def __str__(self):
        return f'{self.label} (x: {self.x}, y: {self.y}, z: {self.z})'


class Jail(models.Model):
    name = models.TextField()
    location_min = models.OneToOneField(Location,
                                        on_delete=models.CASCADE,
                                        related_name='jail_location_min'
                                        )
    location_max = models.OneToOneField(Location,
                                        on_delete=models.CASCADE,
                                        related_name='jail_location_max'
                                        )
    is_max_security = models.BooleanField(default=False)
    prisoner_spawn = models.OneToOneField(Location,
                                          on_delete=models.CASCADE,
                                          related_name='prisoner_spawn'
                                          )

    def __str__(self):
        return self.name


class Town(models.Model):
    name = models.TextField()
    description = models.TextField()
    location = models.OneToOneField(Location,
                                    on_delete=models.CASCADE
                                    )

    def __str__(self):
        return self.name


class Player(models.Model):
    uuid = models.TextField(primary_key=True)
    town = models.ForeignKey(Town,
                             on_delete=models.CASCADE,
                             blank=True,
                             null=True
                             )
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True
                                )
    jail = models.ForeignKey(Jail,
                             on_delete=models.CASCADE,
                             blank=True,
                             null=True
                             )
    is_soldier = models.BooleanField(default=False)
    is_mayor = models.BooleanField(default=False)

    def __str__(self):
        return self.uuid


class Room(models.Model):
    name = models.TextField()
    tax = models.FloatField()
    isSellable = models.BooleanField()
    canBuild = models.BooleanField()
    canDestroy = models.BooleanField()
    town = models.ForeignKey(Town,
                             on_delete=models.CASCADE
                             )
    player = models.ManyToManyField(Player,
                                    blank=True
                                    )
    location_min = models.OneToOneField(Location,
                                        on_delete=models.CASCADE,
                                        related_name='room_location_min'
                                        )
    location_max = models.OneToOneField(Location,
                                        on_delete=models.CASCADE,
                                        related_name='room_location_max'
                                        )

    def __str__(self):
        return self.name


class Prisoner(models.Model):
    prisoner_timer = models.IntegerField()
    player = models.OneToOneField(Player,
                                  on_delete=models.CASCADE
                                  )
    owner = models.ForeignKey(Player,
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True,
                              related_name='owner'
                              )
    jail = models.ForeignKey(Jail,
                             on_delete=models.CASCADE,
                             blank=True,
                             null=True
                             )

    def __str__(self):
        return self.player.uuid


class CriminalRecord(models.Model):
    date = models.DateTimeField(auto_now_add=True,
                                blank=True
                                )
    message = models.TextField()
    player = models.OneToOneField(Player,
                                  on_delete=models.CASCADE
                                  )

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
    related_pages = models.ManyToManyField('self',
                                           blank=True
                                           )
    section = models.ForeignKey(Section,
                                on_delete=models.CASCADE
                                )
    town = models.OneToOneField(Town,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True
                                )

    def __str__(self):
        return self.title

    def clean(self):
        if self.type == 3 and not self.town:
            raise ValidationError(
                'Page with the type of TOWN should have a Town defined'
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Page, self).save(*args, **kwargs)
