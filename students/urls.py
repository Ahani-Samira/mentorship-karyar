from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, create_student


router = DefaultRouter()
router.register(r'students', StudentViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('create', create_student, name='create_student'),
]

# data = '{"first_name": "Asma","last_name": "Ghahramani", "age": "25", "grade":"20"}'
# curl -X POST http://127.0.0.1:8000/api/students/create -H "Content-Type: application/json" -d '{"first_name": "Asma","last_name": "Ghahramani", "age": 25, "grade":20}'