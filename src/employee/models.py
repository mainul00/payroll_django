from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


class Department(models.Model):
    dept_no = models.CharField(_('dept_no'), primary_key=True, max_length=4)
    dept_name = models.CharField(_('name'), unique=True, max_length=40)

    class Meta:
        verbose_name = _('department')
        verbose_name_plural = _('departments')
        db_table = 'departments'
        ordering = ['dept_no']

    def __str__(self):
        return self.dept_name


class DeptEmp(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='emp_no', verbose_name=_('employee'))
    department = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='dept_no', verbose_name=_('department'))

    class Meta:
        verbose_name = _('department employee')
        verbose_name_plural = _('department employees')
        db_table = 'employeedepartments'

    def __str__(self):
        return "{} - {}".format(self.employee, self.department)


class Employee(models.Model):
    emp_no = models.IntegerField(_('employee_number'), primary_key=True)
    birth_date = models.DateField(_('birthday'))
    first_name = models.CharField(_('first name'), max_length=14)
    last_name = models.CharField(_('last name'), max_length=16)
    gender = models.CharField(_('gender'), max_length=1)
    hire_date = models.DateField(_('hire date'))

    class Meta:
        verbose_name = _('employee')
        verbose_name_plural = _('employees')
        db_table = 'employees'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


# class Grade(models.Model):
# 	grade_no  			= models.CharField(_('code'), primary_key=True, max_length=4)
#     # grad_name 			= models.CharField(_('name'), unique=True, max_length=40)
#     basic_salary 		= models.IntegerField()
#     medical_allowance 	= models.IntegerField()
#     lunch_allowance 	= models.IntegerField()
#     transport_bill  	= models.IntegerField()
#     net_salary 			= models.IntegerField()
#     class Meta:
#     	verbose_name = _('grade')
#         verbose_name_plural = _('grades')
#         db_table = 'grade'


class Grade(models.Model):
	grade_no = models.CharField(max_length=10,primary_key=True)
	basic_salary = models.IntegerField()
	medical_allowance = models.IntegerField()
	lunch_allowance = models.IntegerField()
	class Meta:
		verbose_name = _('grade')
		verbose_name_plural= _('grades')
		db_table = 'grades'



class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_no', verbose_name=_('employee'))
    grade    = models.ForeignKey(Grade, on_delete=models.CASCADE, db_column='grade_no', verbose_name=_('grade'))
    from_date = models.DateField(_('from'))
    to_date = models.DateField(_('to'))
    class Meta:
        db_table = 'salaries'
        ordering = ['-from_date']
        verbose_name = _('salary')
        verbose_name_plural = _('salaries')

    def __str__(self):
        return "{} - {}".format(self.employee, self.salary)



class EmployeeDesignation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_no', verbose_name=_('employee'))
    title = models.CharField(_('title'), max_length=50)
    from_date = models.DateField(_('from'))
    to_date = models.DateField(_('to'), blank=True, null=True)

    class Meta:
        verbose_name = _('employeedesignation')
        verbose_name_plural = _('employeedesignations')
        db_table = 'employeedesignations'

    def __str__(self):
        return "{} - {}".format(self.employee, self.title)

# class DeptManager(models.Model):
#     employee = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='emp_no', verbose_name=_('employee'))
#     department = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='dept_no', verbose_name=_('department'))
#     from_date = models.DateField(_('from'))
#     to_date = models.DateField(_('to'))

#     objects = TemporalQuerySet.as_manager()

#     class Meta:
#         verbose_name = _('department manager')
#         verbose_name_plural = _('department managers')
#         db_table = 'dept_manager'
#         ordering = ['-from_date']

#     def __str__(self):
#         return "{} - {}".format(self.employee, self.department)
