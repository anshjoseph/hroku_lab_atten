from django.shortcuts import render,redirect
from ipware import get_client_ip
from .models import day1
import time
#from multiprocessing import Process
"""
feature 


cs_roll = 205502219001
it_roll = 205503319001
email_cs = [ (cs_roll +i) for i in range(41)]
email_it = [ (it_roll +i) for i in range(26)]

"""
address = ["http://127.0.0.1:8000/"]
ip = []
def ipch(val):
    result = False
    if len(ip)>0:
        for i in range(len(ip)):
            if ip[i] == val:
                result = True
            else:
                result = False
    else:
        result = False
    return result
# Create your views here.
def csit_atend(request):
    ip_add,boo = get_client_ip(request)
    ip_add = str(ip_add)
    if ipch(ip_add) == False:
        
        return redirect(address[0])
    data = day1.objects.all()
    return render(request,"show.html",{"data":data})
def error(request):
    add = address[0] + "attend/"
    return render(request,"error.html",{"address":add})
    
def sameip(request):
    ip_add,is_r = get_client_ip(request)
    ip_add = str(ip_add)
    link = address[0]+"attendence/"
    if ipch(ip_add) == False:
        return redirect(address[0])
    else:
        return render(request,'sameip.html',{"link":link})

def atend(request):
    
    ip_add,is_r = get_client_ip(request)
    ip_add = str(ip_add)
    #ip.append(ip_add)
    #print(email_cs)
    if ipch(ip_add):
        return redirect(address[0]+"success/")
    if request.method == "POST":
        name = request.POST.get('name')
        branch = request.POST.get('branch')
        cs_it = [False,False]
        if branch == "it":
            cs_it[0] = True
        else:
            cs_it[1] = True
        #ip.append(ip_add)
        if ipch(ip_add) == False:  
            if len(name) == 0:
                return redirect(address[0]+"error/")  
            if (cs_it[0] or cs_it[1]) == False:
                return redirect(address[0]+"error/")
            day = day1(name=name,it= cs_it[0],cs = cs_it[1])
            day.save()
            ip.append(ip_add)
            return redirect(address[0]+"success/")
        #print(ip)
    return render(request,"attendence.html")