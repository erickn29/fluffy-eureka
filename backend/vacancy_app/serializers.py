from rest_framework import serializers

from .models import StackTool, Language, City, Speciality, \
    Experience, Grade, Company, Vacancy, Profession, Person


class StackToolSerializer(serializers.ModelSerializer):
    """Сериализатор модели"""

    class Meta:
        model = StackTool
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    """Сериализатор модели"""

    class Meta:
        model = Language
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    """Сериализатор модели"""

    class Meta:
        model = City
        fields = '__all__'


class SpecialitySerializer(serializers.ModelSerializer):
    """Сериализатор модели"""

    class Meta:
        model = Speciality
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    """Сериализатор модели"""

    class Meta:
        model = Experience
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    """Сериализатор модели"""

    class Meta:
        model = Grade
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    """Сериализатор модели"""

    class Meta:
        model = Company
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
    """Сериализатор модели"""

    company = CompanySerializer()
    speciality = SpecialitySerializer()
    experience = ExperienceSerializer()
    grade = GradeSerializer()
    language = LanguageSerializer()

    class Meta:
        model = Vacancy
        fields = '__all__'


class ProfessionSerializer(serializers.ModelSerializer):
    """Сериализатор модели"""

    class Meta:
        model = Profession
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    """Сериализатор модели"""

    class Meta:
        model = Person
        fields = '__all__'

