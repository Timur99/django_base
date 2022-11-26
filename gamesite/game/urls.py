from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='gm'),
#    path("g/<int:gameid>/", g)
]