from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from CD.api.models import (
    Location,
    Jail,
    Town,
    Player,
    Room,
    Slave,
    CriminalRecord,
    Section,
    Page,
)
from CD.api.serializers import (
    UserSerializer,
    LocationSerializer,
    JailSerializer,
    TownSerializer,
    RoomSerializer,
    PlayerSerializer,
    SlaveSerializer,
    CriminalRecordSerializer,
    SectionSerializer,
    PageSerializer,
)


class LocationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class JailViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = JailSerializer
    queryset = Jail.objects.all()


class JailLocationMinViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Location.objects.filter(location_min=self.kwargs['jails_pk'])


class JailLocationMaxViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Location.objects.filter(location_max=self.kwargs['jails_pk'])


class JailSlaveSpawnViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Location.objects.filter(slave_spawn=self.kwargs['jails_pk'])


class TownViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TownSerializer
    queryset = Town.objects.all()


class TownLocationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Location.objects.filter(town=self.kwargs['towns_pk'])


class PlayerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


class PlayerTownViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TownSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Town.objects.filter(player=self.kwargs['players_pk'])


class PlayerUserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return User.objects.filter(player=self.kwargs['players_pk'])


class PlayerJailViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = JailSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Jail.objects.filter(player=self.kwargs['players_pk'])


class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomTownViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TownSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Town.objects.filter(room=self.kwargs['rooms_pk'])


class RoomPlayerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlayerSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Player.objects.filter(room=self.kwargs['rooms_pk'])


class RoomLocationMinViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Location.objects.filter(location_min=self.kwargs['rooms_pk'])


class RoomLocationMaxViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Location.objects.filter(location_max=self.kwargs['rooms_pk'])


class SlaveViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SlaveSerializer
    queryset = Slave.objects.all()


class SlavePlayerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlayerSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Player.objects.filter(slave=self.kwargs['slaves_pk'])


class SlaveOwnerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlayerSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Player.objects.filter(owner=self.kwargs['slaves_pk'])


class SlaveJailViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = JailSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Jail.objects.filter(player=self.kwargs['slaves_pk'])


class CriminalRecordViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CriminalRecordSerializer
    queryset = CriminalRecord.objects.all()


class CriminalRecordPlayerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlayerSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Player.objects.filter(
            criminalrecord=self.kwargs['criminalrecords_pk'])


class SectionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SectionSerializer
    queryset = Section.objects.all()


class PageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PageSerializer
    queryset = Page.objects.all()


class PageSectionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SectionSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Section.objects.filter(page=self.kwargs['pages_pk'])
