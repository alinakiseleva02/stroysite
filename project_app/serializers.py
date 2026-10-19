from rest_framework import serializers
from .models import Projects, Employees, Customers, Materials, Teams, Documents, ConstructionObjects

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    # Для чтения (GET) мы хотим видеть вложенные объекты
    employee_details = EmployeeSerializer(source='employee', read_only=True)
    customer_details = CustomerSerializer(source='customer', read_only=True)
    
    # Вычисляемые поля
    formatted_budget = serializers.ReadOnlyField()
    formatted_start_date = serializers.ReadOnlyField()
    formatted_construction_period = serializers.ReadOnlyField()

    class Meta:
        model = Projects
        fields = '__all__' # Включает и id сотрудника/заказчика (для POST/PUT), и details (для GET)

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'

class ConstructionObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionObjects
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'