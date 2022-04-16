from django.urls import path

from .views import home_view,MealCreateView

app_name = 'meal'

urlpatterns = [
    path('',home_view, name='home'),
    path('create/meal/',MealCreateView.as_view(), name='create'),
]
