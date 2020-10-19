from django.urls import path

from apps.quran.views import *

urlpatterns = [
    path('list', ListSura.as_view(), name='list-sura'),
    path('sura/<int:id>', GetSura.as_view(), name='get-sura'),
    path('sura/fa_qomsheei/<int:id>', GetElaheqomsheei.as_view(), name='get-sura-fa'),
    path('ayahtext', SearchSura.as_view(), name='search-sura'),
]
