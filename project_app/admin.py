from django.contrib import admin
from .models import *

admin.site.register(Employees)
admin.site.register(Customers)
admin.site.register(Projects)
admin.site.register(Materials)
admin.site.register(Teams)
admin.site.register(Documents)
admin.site.register(ConstructionObjects)
admin.site.register(MaterialUsage)