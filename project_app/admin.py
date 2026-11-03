from django.contrib import admin
from .models import Projects, Employees, Customers, Materials, Teams, ProjectImage, ContactRequest

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('name', 'customer', 'budget', 'start_date')
    search_fields = ('name',)

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at')
    readonly_fields = ('name', 'phone', 'message', 'created_at')

admin.site.register(Employees)
admin.site.register(Customers)
admin.site.register(Materials)
admin.site.register(Teams)