from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from CD.api.models import (
    Location,
    Jail,
    Town,
    Player,
    Room,
    Prisoner,
    CriminalRecord,
    Section,
    Page,
    Command,
    Argument,
)
from CD.api.serializers import (
    UserSerializer,
    LocationSerializer,
    JailSerializer,
    TownSerializer,
    RoomSerializer,
    PlayerSerializer,
    PrisonerSerializer,
    CriminalRecordSerializer,
    SectionSerializer,
    PageSerializer,
    CommandSerializer,
    ArgumentSerializer,
)


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class JailViewSet(viewsets.ModelViewSet):
    serializer_class = JailSerializer
    queryset = Jail.objects.all()


class JailLocationMinViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Location.objects.filter(
            jail_location_min=self.kwargs['jails_pk'])


class JailLocationMaxViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Location.objects.filter(
            jail_location_max=self.kwargs['jails_pk'])


class JailPrisonerSpawnViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Location.objects.filter(prisoner_spawn=self.kwargs['jails_pk'])


class TownViewSet(viewsets.ModelViewSet):
    serializer_class = TownSerializer
    queryset = Town.objects.all()


class TownLocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Location.objects.filter(town=self.kwargs['towns_pk'])


class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


class PlayerTownViewSet(viewsets.ModelViewSet):
    serializer_class = TownSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Town.objects.filter(player=self.kwargs['players_pk'])


class PlayerUserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return User.objects.filter(player=self.kwargs['players_pk'])


class PlayerJailViewSet(viewsets.ModelViewSet):
    serializer_class = JailSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Jail.objects.filter(player=self.kwargs['players_pk'])


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomTownViewSet(viewsets.ModelViewSet):
    serializer_class = TownSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Town.objects.filter(room=self.kwargs['rooms_pk'])


class RoomPlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Player.objects.filter(room=self.kwargs['rooms_pk'])


class RoomLocationMinViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Location.objects.filter(
            room_location_min=self.kwargs['rooms_pk'])


class RoomLocationMaxViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Location.objects.filter(
            room_location_max=self.kwargs['rooms_pk'])


class PrisonerViewSet(viewsets.ModelViewSet):
    serializer_class = PrisonerSerializer
    queryset = Prisoner.objects.all()


class PrisonerPlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Player.objects.filter(prisoner=self.kwargs['prisoners_pk'])


class PrisonerOwnerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Player.objects.filter(owner=self.kwargs['prisoners_pk'])


class PrisonerJailViewSet(viewsets.ModelViewSet):
    serializer_class = JailSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Jail.objects.filter(player=self.kwargs['prisoners_pk'])


class CriminalRecordViewSet(viewsets.ModelViewSet):
    serializer_class = CriminalRecordSerializer
    queryset = CriminalRecord.objects.all()


class CriminalRecordPlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Player.objects.filter(
            criminalrecord=self.kwargs['criminalrecords_pk'])


class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()


class PageViewSet(viewsets.ModelViewSet):
    serializer_class = PageSerializer
    queryset = Page.objects.all()


class PageSectionViewSet(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Section.objects.filter(page=self.kwargs['pages_pk'])


class CommandViewSet(viewsets.ModelViewSet):
    serializer_class = CommandSerializer
    queryset = Command.objects.all()


class CommandPageViewSet(viewsets.ModelViewSet):
    serializer_class = PageSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Page.objects.filter(command=self.kwargs['commands_pk'])


class ArgumentViewSet(viewsets.ModelViewSet):
    serializer_class = ArgumentSerializer
    queryset = Argument.objects.all()


class ArgumentCommandViewSet(viewsets.ModelViewSet):
    serializer_class = CommandSerializer
    http_method_names = ['get', 'patch', 'put']

    def get_queryset(self):
        return Command.objects.filter(argument=self.kwargs['arguments_pk'])
