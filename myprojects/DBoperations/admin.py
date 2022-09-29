from django.contrib import admin

# Register your models here.
from . models import Family,Employee,Department

# To Customize the Admin Site --

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['Employee_Name','Employee_Salary','Employee_Address','Salary_Type']
    list_filter=['Employee_Address','Employee_Salary']

    def Salary_Type(self,obj):
        if obj.Employee_Salary>75000:
            return 'High Salary'
        else:
            return 'Low Salary'

# First Register the model in Admin Page like this. . . .

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Department)

class FamilyAdmin(admin.ModelAdmin):
    list_display=['FatherName','MotherName','SonName','Daughter_1_Name','Daughter_2_Name']
    list_filter=['id','FatherName']

# First Register the model in Admin Page like this. . . .

admin.site.register(Family,FamilyAdmin)
