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

    city = CitySerializer()

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
    stack = serializers.SerializerMethodField()

    def get_stack(self, obj: Vacancy) -> list | None:
        """Метод возвращает список стека"""
        try:
            data = StackTool.objects.filter(vacancy=obj)
            stack_list = []
            if data:
                for obj in data:
                    stack_list.append(obj.name)
                return stack_list
            return None
        except AttributeError as e:
            print(e)
            return None

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

