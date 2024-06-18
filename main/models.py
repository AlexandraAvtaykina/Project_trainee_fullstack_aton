from django.contrib.auth.models import AbstractUser
from django.db import models


class Client(models.Model):

    STATUS_CHOICES = [
        ('Не в работе', 'Не в работе'),
        ('В работе', 'В работе'),
        ('Отказ', 'Отказ'),
        ('Сделка закрыта', 'Сделка закрыта'),
    ]

    account_number = models.IntegerField(verbose_name='Номер счета')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество')
    birth_date = models.DateField(verbose_name='Дата рождения')
    inn = models.PositiveBigIntegerField(verbose_name='ИНН')
    fullname_of_the_person_responsible = models.ForeignKey('User',
                                                           on_delete=models.CASCADE, verbose_name='ФИО ответственного')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Не в работе', verbose_name='Статус')

    def __str__(self):
        return f' {self.last_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class User(AbstractUser):
    username = None

    fullname = models.CharField(max_length=150, verbose_name='ФИО')
    login = models.CharField(unique=True, max_length=100, verbose_name='Логин')

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f' {self.fullname}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
