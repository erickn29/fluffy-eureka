from django.db.models import QuerySet, Q
from django.http import HttpRequest, HttpResponse
from rest_framework import viewsets

from .models import Vacancy, Grade, Company, Profession, Experience, \
    Speciality, City, Language, StackTool
from .run_parsers import main
from .serializers import VacancySerializer, ProfessionSerializer, \
    CompanySerializer, GradeSerializer, ExperienceSerializer, CitySerializer, \
    SpecialitySerializer, LanguageSerializer, StackToolSerializer


class VacancyViewSet(viewsets.ModelViewSet):
    """Представление вакансий"""

    queryset = Vacancy.objects.get_actual().filter(language__name='Python')
    serializer_class = VacancySerializer

    def get_queryset(self) -> QuerySet:
        """G"""
        queryset = self.queryset
        if len(self.request.GET) > 0:
            data = self.request.query_params
            if data.get('language'):
                queryset = queryset.filter(
                    language=Language.objects.get(
                        name=str(data.get('language'))
                    )
                )
            if data.get('salary_from'):
                salary_from = data.get('salary_from', 0)
                queryset = queryset.filter(
                    Q(salary_from__gte=int(salary_from)) |
                    Q(salary_from=None, salary_to__gte=salary_from))
            if data.get('location'):
                if data.get('location') == 'remote':
                    queryset = queryset.filter(is_remote=True)
                else:
                    location = data.get('location')
                    queryset = queryset.filter(
                        company__city__name=location)
            # if data.get('is_remote') and data.get('is_remote') == 'true':
            #     queryset = queryset.filter(is_remote=True)
            if data.get('experience'):
                experience = data.get('experience')
                queryset = queryset.filter(
                    experience__name=experience
                )
            if data.get('speciality'):
                speciality = data.get('speciality')
                queryset = queryset.filter(
                    speciality__name=speciality
                )
            if data.get('grade'):
                grade = data.get('grade')
                queryset = queryset.filter(grade__name=grade)
        return queryset


class StackToolViewSet(viewsets.ModelViewSet):
    """Представление стека"""

    serializer_class = StackToolSerializer
    queryset = StackTool.objects.all()


class LanguageViewSet(viewsets.ModelViewSet):
    """Представление языка"""

    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class CityViewSet(viewsets.ModelViewSet):
    """Представление города"""

    serializer_class = CitySerializer
    queryset = City.objects.all()


class SpecialityViewSet(viewsets.ModelViewSet):
    """Представление специальности"""

    serializer_class = SpecialitySerializer
    queryset = Speciality.objects.all()


class ExperienceViewSet(viewsets.ModelViewSet):
    """Представление опыта"""

    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()


class GradeViewSet(viewsets.ModelViewSet):
    """Представление грейда"""

    serializer_class = GradeSerializer
    queryset = Grade.objects.all()


class CompanyViewSet(viewsets.ModelViewSet):
    """Представление компаний"""

    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class ProfessionViewSet(viewsets.ModelViewSet):
    """Представление профессии"""

    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()


def get_data(request: HttpRequest) -> HttpResponse:
    """Представление для активации сбора вакансий"""
    main(True, True, True, True)
    return HttpResponse('ok')
