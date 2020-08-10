from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('grader.urls')),
    path('admin/', admin.site.urls),
]
