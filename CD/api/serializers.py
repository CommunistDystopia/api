from django.contrib.auth.models import User
from rest_framework import serializers

from CD.api.models import (
    Location,
    Jail,
    Town,
    Player,
    Slave,
    CriminalRecord,
    Section,
    Page,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
        )


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = (
            'label',
            'x',
            'y',
            'z',
        )


class JailSerializer(serializers.HyperlinkedModelSerializer):
    location_min = serializers.PrimaryKeyRelatedField(many=False,
                                                      read_only=True)
    location_max = serializers.PrimaryKeyRelatedField(many=False,
                                                      read_only=True)
    slave_spawn = serializers.PrimaryKeyRelatedField(many=False,
                                                     read_only=True)

    class Meta:
        model = Jail
        fields = (
            'name',
            'location_min',
            'location_max',
            'is_max_security',
            'slave_spawn',
        )


class TownSerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Town
        fields = (
            'name',
            'description',
            'location'
        )


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    town = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    jail = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Player
        fields = (
            'uuid',
            'town',
            'user',
            'is_soldier',
            'jail',
        )


class SlaveSerializer(serializers.HyperlinkedModelSerializer):
    player = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    owner = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    jail = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Slave
        fields = (
            'slave_timer',
            'player',
            'owner',
            'jail',
        )


class CriminalRecordSerializer(serializers.HyperlinkedModelSerializer):
    player = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = CriminalRecord
        fields = (
            'date',
            'message',
            'player'
        )


class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = (
            'name',
        )


class PageSerializer(serializers.HyperlinkedModelSerializer):
    section = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    town = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    related_pages = serializers.PrimaryKeyRelatedField(many=True,
                                                       read_only=True)

    class Meta:
        model = Page
        fields = (
            'title',
            'body',
            'type',
            'related_pages',
            'section',
            'town'
        )
