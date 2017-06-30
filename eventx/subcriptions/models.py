from django.db import models
from eventx.subcriptions.validators import validate_cpf
from django.shortcuts import resolve_url as r

class Subscription(models.Model):
    name = models.CharField('name', max_length=100, blank=True)
    cpf = models.CharField('cpf', max_length=11, validators=[validate_cpf])
    email = models.EmailField('email', blank=True)
    phone = models.CharField('phone', blank=True, max_length=20)
    created_at = models.DateTimeField('cadastrado em', auto_now_add=True)
    paid = models.BooleanField('pago', default=False)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscrição'
        ordering = ['-created_at']


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('subscriptions:detail', self.pk)