from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.authentication.urls")),

    path("dashboard/", include("apps.dashboard.urls")),
    path("accounts/", include("apps.accounts.urls")),
    path("root/", include("apps.root.urls")),
    path("regi/", include("apps.regi.urls")),

    path("mate/", include("apps.mate.urls")),
    path("cons/", include("apps.cons.urls")),
    path("radi/", include("apps.radi.urls")),
    path("phar/", include("apps.phar.urls")),
    path("labo/", include("apps.labo.urls")),
    # path("ward/", include("apps.ward.urls")),

    # ----------- DRF URLS - APIs __________________________
    path("api/labo/", include("apps.labo.api_labo.urls")),
    path("api/radi/", include("apps.radi.api_radi.urls")),
    # path("api/mate/", include("apps.mate.api_mate.urls")),
    # path("api/ward/", include("apps.ward.api_ward.urls")),
    # path("api/phar/", include("apps.phar.api_phar.urls")),
]


'''
    path("api/regi/", include("apps.regi.api_regis.urls")),
    
    path("api/radio/", include("apps.radio.api_radi.urls")),
    path("api/pharm/", include("apps.pharm.api_pharm.urls")),
    path("api/ward", include("apps.ward.api_ward.urls")),

    # ----------- API TEST --------------------------
    path("api/", include("api.urls")),
    path("frontend/", include("frontend.urls")),
    '''
