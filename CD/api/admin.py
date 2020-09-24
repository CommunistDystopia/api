from django.contrib import admin
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


class RoomAdmin(admin.ModelAdmin):
    filter_horizontal = ('player',)


class PageAdmin(admin.ModelAdmin):
    filter_horizontal = ('related_pages',)


admin.site.register(Location)
admin.site.register(Jail)
admin.site.register(Town)
admin.site.register(Player)
admin.site.register(Room, RoomAdmin)
admin.site.register(Prisoner)
admin.site.register(CriminalRecord)
admin.site.register(Section)
admin.site.register(Page, PageAdmin)
admin.site.register(Command)
admin.site.register(Argument)
