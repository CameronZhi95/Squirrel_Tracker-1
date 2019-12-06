from django.shortcuts import render
from .models import Squirrel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SqForm

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

'''def update(request, Unique_Squirrel_ID):
    sq = Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == 'POST':
        form = SqForm(request.POST, instance=sq)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/(Unique_Squirrel_ID)')
        #check data with form
    else:
        form = SqForm(instance=sq)
        #build empty form

    context = {
        'form':form,
    }

    return render(request,'sightings/update.html',context)'''

def add(request):
    if request.method == 'POST':
        form = SqForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/sightings/add')
        #check data with form
    else:
        form = SqForm()
        #build empty form
    context = {
        'form':form,
    }
    return render(request,'sightings/add.html',context)
