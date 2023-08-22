from django.shortcuts import render
from .models import place, newplace


# Create your views here.

def page1(request):
    obj=place.objects.all()
    obj2=place.objects.all()
    obj3=newplace.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2,'result3':obj3})



#def additions(request):
   # x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
   # add=x+y
  #  neg = x - y
 #   multi = x * y
  #  div = x / y
  #  return render(request,"addition.html",{'result1':add,'result2':neg,'result3':multi,'result4':div})





