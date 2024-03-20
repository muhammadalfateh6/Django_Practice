from django.contrib import admin
from demoapp1.models import Customer_Table, Menu_lemon

# Register your models here.
#admin.site.register(Customer_Table)
admin.site.register(Menu_lemon)

@admin.register(Customer_Table)

class Customer_Table_Admin(admin.ModelAdmin):
    list_display = ('First_name', 'Last_name','Gender','Phone_number', 'Time')