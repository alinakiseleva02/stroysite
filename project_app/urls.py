from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'materials', MaterialViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'objects', ConstructionObjectViewSet)
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]