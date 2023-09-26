from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import seriesform

from .models import tvseries


# Create your views here.
def corp(request):
    seri=tvseries.objects.all()
    return render(request,'index.html',{'series_list':seri})



def series(request,seriesid):
    a=tvseries.objects.get(id=seriesid)
    return render(request,"detail.html",{'kid':a})


def add_series(request):
    if request.method=='POST':
        name = request.POST.get('name',)
        year = request.POST.get('year',)
        desc = request.POST.get('desc',)
        img = request.FILES['img']
        seriesli=tvseries(name=name,year=year,desc=desc,img=img)
        seriesli.save()
        return redirect('/')

    return render(request,'add.html')

def updatef(request,id):
    serie=tvseries.objects.get(id=id)
    form=seriesform(request.POST or None, request.FILES,instance=serie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'series':serie})

def delete(request,id):
    if request.method=='POST':
      quad=tvseries.objects.get(id=id)
      quad.delete()
      return redirect('/')
    return render(request,'delete.html')