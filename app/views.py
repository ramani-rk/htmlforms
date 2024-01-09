from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from app.models import *


def insert_topic (request):
    if request.method=='POST':
        tn=request.POST['tn']

        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()

        QLTO=Topic.objects.all()
        d={'QLTO':QLTO}
        return render(request,'display_topic.html',d)
    return render (request,'insert_topic.html')


def insert_web (request):
    QLTO=Topic.objects.all()
    d={'QLTO' : QLTO}

    if request.method=='POST':
        tn=request.POST['tn']
        n=request.POST['n']
        u=request.POST['u']
        e=request.POST['e']

        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
        WO.save()

        QLWO=Webpage.objects.all()
        d1={'QLWO' : QLWO}

        return render(request,'display_web.html',d1)

    return render(request,'insert_web.html',d)

def insert_accessrecord (request):
    QLWO=Webpage.objects.all()
    d={'QLWO' : QLWO}

    if request.method=='POST':
        n=request.POST['n']
        d=request.POST['d']
        a=request.POST['a']

        WO=Webpage.objects.get(name=n)
        AO=Accessrecord.objects.get_or_create(name=WO,date=d,author=a)[0]
        AO.save()

        QLAO=Accessrecord.objects.all()
        d1={'QLAO' : QLAO}
        return render (request,'display_accessrecord.html',d1)

    return render (request,'insert_accessrecord.html',d)