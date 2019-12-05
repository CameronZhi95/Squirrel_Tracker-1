from django.shortcuts import render
from .models import Squirrel

def sightings_list(request,*args,**kwargs):
    squirrels = Squirrels.objects.all()
    fields = ['Unique_Squirrel_ID','Date','Lat_Long']
    context={
        'squirrels':squirrels,
        'fields':fields,
    }    
    return render(request,'sightings/list.html',context)
