from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Projects, Employees, Customers, Materials, ContactRequest, Services, Reviews
from .serializers import *

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer  

    def get_queryset(self):               
        return super().get_queryset().order_by('-id')  

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Materials.objects.all()
    serializer_class = MaterialSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer

@method_decorator(csrf_exempt, name='dispatch')
class ContactRequestViewSet(viewsets.ModelViewSet):
    queryset = ContactRequest.objects.all().order_by('-created_at')
    serializer_class = ContactRequestSerializer
    permission_classes = [AllowAny]
    authentication_classes = []