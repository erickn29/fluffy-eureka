# from .models import Vacancy, Language, Speciality, Experience, Grade, \
#     City
#
#
# def cities_list():
#     cities = list(
#         City.objects.filter(id__in=[
#             v.id for v in Vacancy.objects.get_actual()
#         ]).values_list('name', flat=True)
#     )
#     return cities
#
#
# def grades_list():
#     grades = list(
#         Grade.objects.filter(id__in=[
#             v.id for v in Vacancy.objects.get_actual()
#         ]).values_list('name', flat=True)
#     )
#     return grades
#
#
# def experiences_list():
#     experiences = list(
#         Experience.objects.filter(id__in=[
#             v.id for v in Vacancy.objects.get_actual()
#         ]).values_list('name', flat=True)
#     )
#     return experiences
#
#
# def specialities_list():
#     specialities = list(
#         Speciality.objects.filter(id__in=[
#             v.id for v in Vacancy.objects.get_actual()
#         ]).values_list('name', flat=True)
#     )
#     return specialities
#
#
# def languages_list():
#     languages = list(
#         Language.objects.filter(id__in=[
#             v.id for v in Vacancy.objects.get_actual()
#         ]).values_list('name', flat=True)
#     )
#     return languages
