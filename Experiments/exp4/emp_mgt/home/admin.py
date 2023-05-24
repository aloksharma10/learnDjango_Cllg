from django.contrib import admin
from home.models import Role, Employee, Department

# Register your models here.

admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Employee)