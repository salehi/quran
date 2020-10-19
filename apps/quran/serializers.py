from django.contrib.auth.models import User, Group
from rest_framework import serializers

from apps.quran.models import Quran, QuranSuraNames, QuranPersianElaheqomsheei


# ARABIC
class ArabicVerse(serializers.ModelSerializer):
    class Meta:
        model = Quran
        # fields = '__all__'
        exclude = ["id", "databaseid", "suraid"]


class ArabicSearch(ArabicVerse):
    sura = serializers.SerializerMethodField()

    def get_sura(self, quran):
        assert isinstance(quran, Quran)
        return ListArabic(QuranSuraNames.objects.get(id=quran.suraid)).data


class ListArabic(serializers.ModelSerializer):
    class Meta:
        model = QuranSuraNames
        fields = '__all__'


class GetArabic(serializers.ModelSerializer):
    class Meta:
        model = QuranSuraNames
        fields = '__all__'

    verses = serializers.SerializerMethodField()

    def get_verses(self, sura):
        return ArabicVerse(Quran.objects.filter(suraid=sura.id).order_by('verseid'),
                           many=True,
                           read_only=True).data


# Farsi Translation
class FarsiVerseQomsheei(serializers.ModelSerializer):
    class Meta:
        model = QuranPersianElaheqomsheei
        exclude = ["id", "databaseid", "suraid"]


class ListFarsi(serializers.ModelSerializer):
    class Meta:
        model = QuranSuraNames
        fields = '__all__'


class GetFarsi(serializers.ModelSerializer):
    class Meta:
        model = QuranSuraNames
        fields = '__all__'

    verses = serializers.SerializerMethodField()

    def get_verses(self, sura):
        return FarsiVerseQomsheei(
            Quran.objects.filter(suraid=sura.id).order_by('verseid'),
            many=True,
            read_only=True).data
