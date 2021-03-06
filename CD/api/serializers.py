from django.contrib.auth.models import User
from rest_framework import serializers

from CD.api.models import (
    Location,
    Jail,
    Town,
    Player,
    Prisoner,
    Room,
    CriminalRecord,
    Section,
    Page,
    Command,
    Argument,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
        )


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = (
            'id',
            'label',
            'x',
            'y',
            'z',
        )


class JailSerializer(serializers.HyperlinkedModelSerializer):
    location_min = serializers.PrimaryKeyRelatedField(many=False,
                                                      read_only=False,
                                                      queryset=Location.objects.all()
                                                      )
    location_max = serializers.PrimaryKeyRelatedField(many=False,
                                                      read_only=False,
                                                      queryset=Location.objects.all()
                                                      )
    prisoner_spawn = serializers.PrimaryKeyRelatedField(many=False,
                                                        read_only=False,
                                                        queryset=Location.objects.all()
                                                        )

    class Meta:
        model = Jail
        fields = (
            'id',
            'name',
            'location_min',
            'location_max',
            'is_max_security',
            'prisoner_spawn',
        )


class TownSerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.PrimaryKeyRelatedField(many=False,
                                                  read_only=False,
                                                  queryset=Location.objects.all()
                                                  )

    class Meta:
        model = Town
        fields = (
            'id',
            'name',
            'description',
            'location'
        )


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    town = serializers.PrimaryKeyRelatedField(many=False,
                                              read_only=False,
                                              queryset=Town.objects.all()
                                              )
    user = serializers.PrimaryKeyRelatedField(many=False,
                                              read_only=False,
                                              queryset=User.objects.all()
                                              )
    jail = serializers.PrimaryKeyRelatedField(many=False,
                                              read_only=False,
                                              queryset=Jail.objects.all()
                                              )

    class Meta:
        model = Player
        fields = (
            'uuid',
            'town',
            'user',
            'jail',
            'is_soldier',
            'is_mayor',
        )


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    town = serializers.PrimaryKeyRelatedField(many=False,
                                              read_only=False,
                                              queryset=Town.objects.all()
                                              )
    player = serializers.PrimaryKeyRelatedField(many=True,
                                                read_only=False,
                                                queryset=Player.objects.all()
                                                )
    location_min = serializers.PrimaryKeyRelatedField(many=False,
                                                      read_only=False,
                                                      queryset=Location.objects.all()
                                                      )
    location_max = serializers.PrimaryKeyRelatedField(many=False,
                                                      read_only=False,
                                                      queryset=Location.objects.all()
                                                      )

    class Meta:
        model = Room
        fields = (
            'id',
            'name',
            'tax',
            'town',
            'player',
            'location_min',
            'location_max'
        )


class PrisonerSerializer(serializers.HyperlinkedModelSerializer):
    player = serializers.PrimaryKeyRelatedField(many=False,
                                                read_only=False,
                                                queryset=Player.objects.all()
                                                )
    owner = serializers.PrimaryKeyRelatedField(many=False,
                                               read_only=False,
                                               queryset=Player.objects.all()
                                               )
    jail = serializers.PrimaryKeyRelatedField(many=False,
                                              read_only=False,
                                              queryset=Jail.objects.all()
                                              )

    class Meta:
        model = Prisoner
        fields = (
            'id',
            'prisoner_timer',
            'player',
            'owner',
            'jail',
        )


class CriminalRecordSerializer(serializers.HyperlinkedModelSerializer):
    player = serializers.PrimaryKeyRelatedField(many=False,
                                                read_only=False,
                                                queryset=Player.objects.all()
                                                )

    class Meta:
        model = CriminalRecord
        fields = (
            'id',
            'date',
            'message',
            'player'
        )


class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = (
            'id',
            'name',
        )


class PageSerializer(serializers.HyperlinkedModelSerializer):
    section = serializers.PrimaryKeyRelatedField(many=False,
                                                 read_only=False,
                                                 queryset=Section.objects.all()
                                                 )
    town = serializers.PrimaryKeyRelatedField(many=False,
                                              read_only=False,
                                              queryset=Town.objects.all()
                                              )
    related_pages = serializers.PrimaryKeyRelatedField(many=True,
                                                       read_only=False,
                                                       queryset=Page.objects.all()
                                                       )

    class Meta:
        model = Page
        fields = (
            'id',
            'title',
            'type',
            'related_pages',
            'section',
            'town'
        )


class CommandSerializer(serializers.HyperlinkedModelSerializer):
    page = serializers.PrimaryKeyRelatedField(many=False,
                                              read_only=False,
                                              queryset=Page.objects.all()
                                              )

    class Meta:
        model = Command
        fields = (
            'id',
            'name',
            'description',
            'usage',
            'permission',
            'role',
            'page'
        )


class ArgumentSerializer(serializers.HyperlinkedModelSerializer):
    command = serializers.PrimaryKeyRelatedField(many=False,
                                                 read_only=False,
                                                 queryset=Command.objects.all()
                                                 )

    class Meta:
        model = Argument
        fields = (
            'id',
            'name',
            'description',
            'command',
        )
