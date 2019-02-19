# Generated by Django 2.1.7 on 2019-02-19 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_no', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='dept_no')),
                ('dept_name', models.CharField(max_length=40, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'department',
                'verbose_name_plural': 'departments',
                'db_table': 'departments',
                'ordering': ['dept_no'],
            },
        ),
        migrations.CreateModel(
            name='DeptEmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(db_column='dept_no', on_delete=django.db.models.deletion.CASCADE, to='employee.Department', verbose_name='department')),
            ],
            options={
                'verbose_name': 'department employee',
                'verbose_name_plural': 'department employees',
                'db_table': 'employeedepartments',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_no', models.IntegerField(primary_key=True, serialize=False, verbose_name='employee_number')),
                ('birth_date', models.DateField(verbose_name='birthday')),
                ('first_name', models.CharField(max_length=14, verbose_name='first name')),
                ('last_name', models.CharField(max_length=16, verbose_name='last name')),
                ('gender', models.CharField(max_length=1, verbose_name='gender')),
                ('hire_date', models.DateField(verbose_name='hire date')),
            ],
            options={
                'verbose_name': 'employee',
                'verbose_name_plural': 'employees',
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='EmployeeDesignation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('from_date', models.DateField(verbose_name='from')),
                ('to_date', models.DateField(blank=True, null=True, verbose_name='to')),
                ('employee', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, to='employee.Employee', verbose_name='employee')),
            ],
            options={
                'verbose_name': 'employeedesignation',
                'verbose_name_plural': 'employeedesignations',
                'db_table': 'employeedesignations',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('grade_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('basic_salary', models.IntegerField()),
                ('medical_allowance', models.IntegerField()),
                ('lunch_allowance', models.IntegerField()),
            ],
            options={
                'verbose_name': 'grade',
                'verbose_name_plural': 'grades',
                'db_table': 'grades',
            },
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(verbose_name='from')),
                ('to_date', models.DateField(verbose_name='to')),
                ('employee', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, to='employee.Employee', verbose_name='employee')),
                ('grade', models.ForeignKey(db_column='grade_no', on_delete=django.db.models.deletion.CASCADE, to='employee.Grade', verbose_name='grade')),
            ],
            options={
                'verbose_name': 'salary',
                'verbose_name_plural': 'salaries',
                'db_table': 'salaries',
                'ordering': ['-from_date'],
            },
        ),
        migrations.AddField(
            model_name='deptemp',
            name='employee',
            field=models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, to='employee.Employee', verbose_name='employee'),
        ),
    ]
