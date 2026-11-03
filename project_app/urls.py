from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'materials', MaterialViewSet)
router.register(r'teams', TeamViewSet)

# ВОТ ЭТА СТРОЧКА ОТВЕЧАЕТ ЗА ЗАЯВКИ:
router.register(r'contacts', ContactRequestViewSet) 

urlpatterns = [
    # Обратите внимание: здесь должно быть ПУСТО '', а не 'api/'
    path('', include(router.urls)), 
]