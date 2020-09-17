from django.urls import include, path
from rest_framework_nested import routers
from CD.api import views

router = routers.DefaultRouter()

# Location
router.register(r'locations', views.LocationViewSet)

# Jail
router.register(r'jails', views.JailViewSet)
jails_router = routers.NestedSimpleRouter(router, r'jails',
                                          lookup='jails')
jails_router.register(r'location_min', views.JailLocationMinViewSet,
                      basename='location_min')
jails_router.register(r'location_max', views.JailLocationMaxViewSet,
                      basename='location_max')
jails_router.register(r'slave_spawn', views.JailSlaveSpawnViewSet,
                      basename='slave_spawn')

# Town
router.register(r'towns', views.TownViewSet)
towns_router = routers.NestedSimpleRouter(router, r'towns',
                                          lookup='towns')
towns_router.register(r'location', views.TownLocationViewSet,
                      basename='location')

# Player
router.register(r'players', views.PlayerViewSet)
players_router = routers.NestedSimpleRouter(router, r'players',
                                            lookup='players')
players_router.register(r'town', views.PlayerTownViewSet,
                        basename='town')
players_router.register(r'user', views.PlayerUserViewSet,
                        basename='user')
players_router.register(r'jail', views.PlayerJailViewSet,
                        basename='jail')

# Slave
router.register(r'slaves', views.SlaveViewSet)
slaves_router = routers.NestedSimpleRouter(router, r'slaves',
                                           lookup='slaves')
slaves_router.register(r'player', views.SlavePlayerViewSet,
                       basename='player')
slaves_router.register(r'owner', views.SlaveOwnerViewSet,
                       basename='owner')
slaves_router.register(r'jail', views.SlaveJailViewSet,
                       basename='jail')

# CriminalRecord
router.register(r'criminalrecords', views.CriminalRecordViewSet)
criminalrecords_router = routers.NestedSimpleRouter(router, r'criminalrecords',
                                                    lookup='criminalrecords')
criminalrecords_router.register(r'player', views.CriminalRecordPlayerViewSet,
                                basename='player')

# Section
router.register(r'sections', views.SectionViewSet)

# Page
router.register(r'pages', views.PageViewSet)
pages_router = routers.NestedSimpleRouter(router, r'pages', lookup='pages')
pages_router.register(r'section', views.PageSectionViewSet,
                      basename='section')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('', include(jails_router.urls)),
    path('', include(towns_router.urls)),
    path('', include(players_router.urls)),
    path('', include(slaves_router.urls)),
    path('', include(criminalrecords_router.urls)),
    path('', include(pages_router.urls)),
]
