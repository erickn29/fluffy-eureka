from rest_framework import viewsets

from .models import Vacancy, Grade, Company, Profession, Experience, \
    Speciality, City, Language, StackTool
from .serializers import VacancySerializer, ProfessionSerializer, \
    CompanySerializer, GradeSerializer, ExperienceSerializer, CitySerializer, \
    SpecialitySerializer, LanguageSerializer, StackToolSerializer


class VacancyViewSet(viewsets.ModelViewSet):
    """Представление вакансий"""

    queryset = Vacancy.objects.get_actual().filter(language__name='Python')
    serializer_class = VacancySerializer

    # def get_queryset(self):
    #     pass


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
