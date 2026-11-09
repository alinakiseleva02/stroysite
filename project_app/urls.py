from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project') 
router.register(r'employees', EmployeeViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'materials', MaterialViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'contacts', ContactRequestViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]