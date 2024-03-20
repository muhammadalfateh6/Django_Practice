from django.contrib import admin
from mainmenu import models


# Register your models here.
admin.site.register(models.MenuCategory)
admin.site.register(models.Menu)
