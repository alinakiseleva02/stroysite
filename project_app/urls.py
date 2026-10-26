from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'materials', MaterialViewSet) # <--- Проверьте, что эта строчка ЕСТЬ
router.register(r'teams', TeamViewSet)
router.register(r'objects', ConstructionObjectViewSet)
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    # ВАЖНО: здесь должно быть ПУСТО, так как 'api/' мы уже добавили в главном файле project/urls.py
    path('', include(router.urls)), 
]