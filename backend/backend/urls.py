from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/post/', include('article_app.urls')),
    path('api/v1/vacancy/', include('vacancy_app.urls')),
]
