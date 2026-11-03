from rest_framework import serializers
from .models import Projects, Employees, Customers, Materials, Teams, ProjectImage, ContactRequest

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image']

class ProjectSerializer(serializers.ModelSerializer):
    employee_details = EmployeeSerializer(source='employee', read_only=True)
    customer_details = CustomerSerializer(source='customer', read_only=True)
    gallery = ProjectImageSerializer(many=True, read_only=True)
    
    formatted_budget = serializers.ReadOnlyField()
    formatted_start_date = serializers.ReadOnlyField()
    formatted_construction_period = serializers.ReadOnlyField()

    class Meta:
        model = Projects
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'

class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = '__all__'