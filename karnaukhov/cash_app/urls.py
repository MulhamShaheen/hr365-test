from django.urls import path
from .views import get_course


urlpatterns = [
    path('rates/', get_course),
]
