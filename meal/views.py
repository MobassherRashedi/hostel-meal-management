from django.shortcuts import render
from django.contrib.auth import get_user_model
import calendar
from .models import Meal,Product,Expenses
from django.urls import reverse_lazy
from .forms import MealModelForm
from django.views.generic import CreateView,UpdateView,DeleteView

def home_view(request):
    User = get_user_model()
    all_user = User.objects.all()

    import datetime
    import calendar
    # current date
    year_month_day = datetime.date.today()

    # month name
    year_month_day = str(year_month_day)
    year,month,day = year_month_day.split("-")
    year = int(year)
    month = int(month)
    day = int(day)
    month_name = calendar.month_name[month]

    #last day of month
    last_day = int(calendar.monthrange(year, month)[1])

    month_day_list=[i for i in range(1,last_day+1)]

    # collecting user Meal data and mapping to month date
    import json
    from django.core import serializers

    js_data = serializers.serialize("python",Meal.objects.all(),fields=('total_meal','user','date'))
    jsn_data = serializers.serialize("json",Meal.objects.all(),fields=('total_meal','user','date'))
    jsn_data_in = json.dumps(jsn_data,indent=2)
    data = json.loads(jsn_data_in)



    temp_dict=dict()

    for each in Meal.objects.all():
        x = each.date.today()
        temp_day = x.day
        if temp_day not in temp_dict: 
            temp_dict[temp_day] = []
            temp_dict[temp_day].append(each.total_meal)
    


    print("===================================")
    print(temp_dict)


    test_data={'1':[2,3,4,0],'2':[1,2,2,0],'3':[0,2,0,4],'4':[0,2,0,4],'5':[0,2,0,4],'6':[0,2,0,4],'7':[0,2,0,4]}
    context={
        "all_user":all_user,
        "current_year":year,
        "current_month_number":month,
        "current_month_name":month_name,
        "current_day":day,
        "last_day_of_the_month":last_day,
        "month_day_list":month_day_list,
        "data":data,
        "test_data":test_data.items(),

    }
    return render(request,'meal/home.html',context=context)

class MealCreateView(CreateView):
    model = Meal
    form_class = MealModelForm
    template_name = 'meal/create.html'
    success_url = reverse_lazy('meal:home')


    def form_valid(self,form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)

class ProductCreateView(CreateView):
    model = Product
    template_name = 'meal/product.html'
