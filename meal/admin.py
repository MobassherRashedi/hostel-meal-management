from django.contrib import admin
from .models import Meal,Product,Expenses

class MealModelAdmin(admin.ModelAdmin):
    list_display  = ['date','user','meal_number','guest_meal','total_meal']
    #exclude = ('total_meal',)
    list_filter = ('user', 'date',)

class ExpensesModelAdmin(admin.ModelAdmin):
    list_display = ['id','date','user','total_amount']

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name','quantity','amount','date','user']

admin.site.register(Meal,MealModelAdmin)
admin.site.register(Product,ProductModelAdmin)
admin.site.register(Expenses,ExpensesModelAdmin)

