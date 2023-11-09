from django.shortcuts import render
from .models import *


def home(request):
    categories=food_category.objects.all()
    foods=food.objects.all()
    objects=[]
    for cat in categories:
        cat_foods=[]
        for foo in foods:
            if foo.category == cat:
                cat_foods.append(foo)
        if cat_foods!=[]:
            objects.append({"category":cat,"foods":cat_foods})
    context={"objects":objects}
    return render(request,"index.html",context)
# Create your views here.
