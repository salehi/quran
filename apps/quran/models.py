# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from enum import Enum

from django.db import models
from django.utils.translation import ugettext_lazy as _

VERBOSE_NAME = _('Quran')


class Quran(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    databaseid = models.SmallIntegerField(db_column='DatabaseID')  # Field name made lowercase.
    suraid = models.IntegerField(db_column='SuraID')  # Field name made lowercase.
    verseid = models.IntegerField(db_column='VerseID')  # Field name made lowercase.
    ayahtext = models.TextField(db_column='AyahText')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Quran'


class QuranPersianElaheqomsheei(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    databaseid = models.SmallIntegerField(db_column='DatabaseID')  # Field name made lowercase.
    suraid = models.IntegerField(db_column='SuraID')  # Field name made lowercase.
    verseid = models.IntegerField(db_column='VerseID')  # Field name made lowercase.
    ayahtext = models.TextField(db_column='AyahText')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Quran_persian_elaheqomsheei'


class QuranSuraNames(models.Model):
    class Place_of_Revelation(Enum):
        Mecca = str("مکه")
        Medina = str("مدینه")

        @staticmethod
        def choices():
            choices = [(member.value, member.value)
                       for name, member in
                       __class__.__members__.items()]
            return choices

    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.TextField('Name', help_text=_("Sura Name"))
    place_of_revelation = models.TextField('Place_of_Revelation',
                                           choices=Place_of_Revelation.choices(),
                                           help_text=_("Place of revelation"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Quran_sura_name_farsi'
        verbose_name = _('Sura Name')
        verbose_name_plural = _('Sura Names')
