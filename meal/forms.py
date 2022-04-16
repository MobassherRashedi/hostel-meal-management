from .models import Meal,Product,Expenses
from django import forms


class MealModelForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ["meal_number","guest_meal","date"]