from django.apps import AppConfig

class MealConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'meal'

"""
---------------------------------------
just importing the signals module inside the ready() 
method will work because I’m using the @receiver() decorator.
If you are connecting the receiver function using the connect() method,
refer to the example below:
---------------------------------------

from cmdbox.profiles.signals import total_meal_counter
from django.contrib.auth import get_user_model

class ProfilesConfig(AppConfig):
    name = 'cmdbox.profiles'
    verbose_name = _('profiles')

    def ready(self):
        post_save.connect(total_meal_counter, sender=get_user_model())


"""