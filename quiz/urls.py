from django.contrib import admin
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("users.urls")),
    path("quiz/", include("questions.urls")),
]