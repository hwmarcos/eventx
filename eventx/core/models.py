from django.db import models
from django.shortcuts import resolve_url as r

from eventx.core.managers import KindQuerySet, PeriodManager


class Speaker(models.Model):
    name = models.CharField('Nome', max_length=255)
    slug = models.SlugField('Slug')
    photo = models.URLField('Foto')
    website = models.URLField('Site', blank=True)
    description = models.TextField('Descrição', blank=True)

    class Meta:
        verbose_name = 'Palestrante'
        verbose_name_plural = 'Palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)

class Contact(models.Model):

    EMAIL = 'E'
    PHONE = 'P'

    KINDS = (
        (EMAIL, 'Email'),
        (PHONE, 'Telefone')
    )

    speaker = models.ForeignKey('Speaker', verbose_name='Palestrante')
    kind = models.CharField('tipo', max_length=1, choices=KINDS)
    value = models.CharField('valor', max_length=255)

    objects = KindQuerySet.as_manager()

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'


class Activity(models.Model):
    title = models.CharField('Título', max_length=100)
    start = models.TimeField('Inicio', blank=True, null=True)
    description = models.TextField('Descrição', blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name='Palestrantes', blank=True)

    objects = PeriodManager()

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
        verbose_name = 'Palestra'
        verbose_name_plural = 'Palestras'

class Talk(Activity):
    pass

class Course(Activity):
    slots = models.IntegerField()

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'