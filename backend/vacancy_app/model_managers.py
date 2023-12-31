from datetime import timedelta, datetime

from django.db import models
from django.db.models import Q, QuerySet


class CustomVacancyManager(models.Manager):
    """Менеджер для модели вакансий"""

    def get_actual(self) -> QuerySet:
        """Метод возвращает вакансии, опубликованные за последние 30 дней"""
        start_date = datetime.now().date() - timedelta(days=300)
        end_date = datetime.now().date()
        return self.filter(
            Q(date__range=[start_date, end_date]) &
            Q(
                Q(salary_from__isnull=False) | Q(salary_to__isnull=False)
            )
        )

    def get_python(self) -> QuerySet:
        """Метод возвращает только Python вакансии"""
        return self.filter(
            language__name='Python'
        )
