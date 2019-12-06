from django.shortcuts import render
from .models import Squirrel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def sightings_list(request):
    squirrels = Squirrel.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(squirrels, 20)
    try:
    	numbers = paginator.page(page)
    except PageNotAnInteger:
    	numbers = paginator.page(1)
    except EmptyPage:
    	numbers = paginator.page(paginator.num_pages)
    return render(request,'sightings/list.html',{'numbers':numbers})
