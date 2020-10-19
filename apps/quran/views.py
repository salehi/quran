from django.db.models import QuerySet
from django_filters.rest_framework import FilterSet, DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import RetrieveAPIView, ListAPIView

from apps.quran.serializers import *


class ListSura(ListAPIView):
    queryset = QuranSuraNames.objects.all()
    serializer_class = ListArabic


class GetSura(RetrieveAPIView):
    queryset = QuranSuraNames.objects.all()
    serializer_class = GetArabic
    lookup_field = 'id'


class GetElaheqomsheei(RetrieveAPIView):
    queryset = QuranPersianElaheqomsheei.objects.all()
    serializer_class = FarsiVerseQomsheei
    lookup_field = 'id'


class InAyehSearch(FilterSet):
    class Meta:
        model = Quran
        fields = ['ayahtext']


class SearchSura(ListAPIView):
    queryset = Quran.objects.all()
    serializer_class = ArabicSearch
    filter_backends = [filters.SearchFilter]
    search_fields = ['ayahtext']