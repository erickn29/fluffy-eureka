from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'stacktool', views.StackToolViewSet)
router.register(r'language', views.LanguageViewSet)
router.register(r'city', views.CityViewSet)
router.register('speciality', views.SpecialityViewSet)
router.register(r'experience', views.ExperienceViewSet)
router.register(r'grade', views.GradeViewSet)
router.register(r'company', views.CompanyViewSet)
router.register(r'profession', views.ProfessionViewSet)
router.register(r'vacancy', views.VacancyViewSet)

urlpatterns = router.urls
