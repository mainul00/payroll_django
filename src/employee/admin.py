from django.contrib import admin
from .models import Salary,Employee,Grade,Designation,Department,EmployeeDesignation,DepartmentEmployee

admin.site.register(Salary)
admin.site.register(Employee)
admin.site.register(Grade)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(EmployeeDesignation)
admin.site.register(DepartmentEmployee)

