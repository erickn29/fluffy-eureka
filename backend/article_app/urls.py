from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'post', views.ArticleViewSet)

urlpatterns = router.urls

