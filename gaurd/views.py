from django.shortcuts import render,redirect
from gaurd.models import gaurd
from gaurd.models import guest_detail
import datetime

# Create your views here.

def gaurds(request):
    if request.session.get('gname'):
        return redirect('ghome')
    else:
        return render(request,'glogin.html')
    
def glogin(request):
    gname = request.POST['gname']
    gpass = request.POST['gpass']
    
    res = gaurd.objects.filter(gname=gname , gpass=gpass)
    
    if len(res)==1:
        request.session['gname']=res[0].gname
        return redirect('ghome')
    else:
        return render(request,'glogin.html',{'msg':'Username or password is incorrect !!!!'})
        
def ghome(request):
    if request.session.get('gname'):
        return render(request,'gaurd.html',)
    else:
        return redirect('/gaurd/')
        
def glogout(request):
    del request.session['gname']
    return redirect('/gaurd/')
    
def insert(request):
    if request.session.get('gname'):
        return render(request,'insert.html')
    else:
        return redirect('/gaurd/')
        
def enter(request):
    guest = request.POST['guest']
    pur = request.POST['pur']
    camefrom = request.POST['camefrom']
    
    intime = datetime.datetime.now().replace(microsecond=0)
    
    qu = guest_detail(intime=intime , guest=guest , pur=pur , camefrom=camefrom)
    qu.save()

    return render(request,'insert.html',{'msg':'Entry has been done successfully !!!'})
    
def exit(request):
    if request.session.get('gname'):
        res = guest_detail.objects.all()
        return render(request,'entry.html',{'res':res})
    else:
        return redirect('/gaurd/')
        
def update_exit(request):
    id = request.GET['id']
    extime = datetime.datetime.now().replace(microsecond=0)
    res = guest_detail.objects.get(id=id)
    res.extime = extime 
    res.save()
    return render(request,'updated.html',{'msg':'Exit updated successfully!!!!' ,})
    
def chk_entry(request):
    if request.session.get('gname'):
        res = guest_detail.objects.all()
        return render(request,'updated.html',{'res':res})
    else:
        return redirect('/gaurd/')
        
    
    