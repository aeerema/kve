from django.db import models
from django.utils.translation import gettext_lazy as gtl

from .family import Family
from .genus import Genus

class Language(models.Model):
    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"
    
    class TenseSystem(models.TextChoices):
        f = "fut",   gtl("fut / non-fut")
        p = "pst",   gtl("pst / non-pst")
        t = "three", gtl("three-part") 
        n = "not",   gtl("no tenses")
        __empty__ =  gtl("(Unknown)")
    
    class TenseMarker(models.TextChoices):
        m = "Mrph", gtl("Морфологический")
        a = "Anlt", gtl("Аналитический")
        b = "Both", gtl("Возможны оба") 
        n = "None", gtl("Ни одного")
        __empty__ = gtl("(Unknown)")

    class CombOptionState(models.TextChoices):
        Y = "YES",       gtl("Подтверждённое да")
        N = "not found", gtl("Кажется нет")
        Q = "?",         gtl("Непонятно")
        T = "---",       gtl("Невозможно") 
        __empty__ =      gtl("(Unknown)")

    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)

    genus = models.ForeignKey(Genus, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    
    tense_system = models.CharField(max_length=10, choices=TenseSystem, blank=True)
    fut = models.CharField(max_length=10, choices=TenseMarker, blank=True)
    pst = models.CharField(max_length=10, choices=TenseMarker, blank=True)

    mm = models.CharField(max_length=10, choices=CombOptionState, blank=True)
    ma = models.CharField(max_length=10, choices=CombOptionState, blank=True)
    am = models.CharField(max_length=10, choices=CombOptionState, blank=True)
    aa = models.CharField(max_length=10, choices=CombOptionState, blank=True)

    main_comment = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name
