# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from custom_user.models import EmailUser as User


# Create your models here.

class Post(models.Model):
    """Post model"""

    title = models.CharField(
        max_length=130,
        verbose_name=u'Заголовок')

    body = models.TextField(
        verbose_name=u'Опис')

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=u'Дата створення')

    author = models.ForeignKey(User,
        verbose_name=u'Автор',
        null=True)

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u"Пости"
