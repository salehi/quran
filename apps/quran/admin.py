from django.contrib import admin

from apps.quran.models import QuranSuraNames


@admin.register(QuranSuraNames)
class QuranSuraNamesAdmin(admin.ModelAdmin):
    pass