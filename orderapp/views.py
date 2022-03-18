from django.http import HttpResponse
from django.shortcuts import render
from  datetime import  datetime,time
import json
from .models import order
import pytz
# Create your views here.
def index(request):
    return render(request,"index.html")
def cart(request):
    start1=time(9,0,0)
    end1=time(12,0,0)
    start2=time(17,0,0)
    end2=time(22,0,0)   
    if (start1<= datetime.now(tz=pytz.timezone('Asia/Kolkata')).time()  <=end1) or (start2<= datetime.now().time()  <=end2): 
        return render(request,"cart.html",{"time":1})
    else:
        return render(request,"cart.html")
def placeorder(request):
    
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        address=request.POST.get("address")
        price=request.POST.get("price")
        products=json.loads(request.POST.get("products"))
        o=order(name=name,email=email,phone=phone,address=address,price=price,products=products)
        o.save()
        return render(request,"form.html",{"model":1})
    else:
        return render(request,"form.html")
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')