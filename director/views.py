from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import database
from gaurd.models import gaurd
from gaurd.models import guest_detail

# Create your views here.

def director(request):
    if request.session.get('dname'):
        return redirect('dhome')
    else:    
        return render(request,'home.html')

def login(request):
    dname = request.POST['dname']
    dpass = request.POST['dpass']
    
    res = database.objects.filter(dname=dname , dpass=dpass)
    
    if len(res)==1:
        request.session['dname']=res[0].dname
        return redirect('dhome') 
    else:
        return render(request,'home.html',{'fail':'Username or Password is Incorrect!!!!'})
        
def dhome(request):
        if request.session.get('dname'):
            return render(request,'jk.html')
        else:
            return redirect('/director/')

def logout(request):
    del request.session['dname']
    return redirect('/director/')
        
def create(request):
    if request.session.get('dname'):
        return render(request,'glog.html')
    else:
        return redirect('/director/')
        
def create_account(request):
    gname = request.POST['gname']
    fname = request.POST['fname']
    lname = request.POST['lname']
    gpass = request.POST['gpass']
    
    res = gaurd.objects.filter(gname=gname)

    if len(res)>0:
        return render(request,'glog.html',{'msg':'User name already exist!!!!'})
    else:
        q = gaurd(gname=gname , fname=fname , lname=lname , gpass=gpass)
        q.save()
        return render(request,'glog.html',{'msg':'Account created successfully!!!!'})
        
def checkentry(request):
    if request.session.get('dname'):
        res = guest_detail.objects.all()
        return render(request,'d_updated.html',{'res':res})
    else:
        return redirect('/director/')
    
        

        



        