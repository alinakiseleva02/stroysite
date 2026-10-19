from rest_framework import viewsets
from .models import Projects, Employees, Customers, Materials, Teams, Documents, ConstructionObjects
from .serializers import *

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all().order_by('-id')
    serializer_class = ProjectSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Materials.objects.all()
    serializer_class = MaterialSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer

class ConstructionObjectViewSet(viewsets.ModelViewSet):
    queryset = ConstructionObjects.objects.all()
    serializer_class = ConstructionObjectSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentSerializer