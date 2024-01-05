from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'post', views.ArticleViewSet)
router.register(r'', views.ArticleViewSet)

urlpatterns = router.urls

