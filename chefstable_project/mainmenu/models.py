from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length= 200)
    Taste = models.CharField(max_length= 200, null=True)


class Menu(models.Model):
    menu_item = models.CharField(max_length = 50)
    price = models.IntegerField(null = False)
    the_key = models.ForeignKey(MenuCategory, on_delete = models.PROTECT, default = None)


