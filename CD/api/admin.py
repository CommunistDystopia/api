from django.contrib import admin
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

admin.site.register(Location)
admin.site.register(Jail)
admin.site.register(Town)
admin.site.register(Player)
admin.site.register(Room)
admin.site.register(Slave)
admin.site.register(CriminalRecord)
admin.site.register(Section)
admin.site.register(Page)
