from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('', include('apps.core.urls')),
    path('budget/', include('apps.budget.urls')),
    path('mileage/', include('apps.mileage.urls')),
    path('episodetracker/', include('apps.episodetracker.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns