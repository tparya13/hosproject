from django.shortcuts import render,HttpResponse,redirect
from .models import Homes,Branch,Gallery,Blog,Package,Enquery,Appointment,Contact,Testi
# Create your views here.
def Home(request):
    homes=Homes.objects.all()
    testi=Testi.objects.all()
    if request.method=="POST": 
        names=request.POST.get('names','')
        email=request.POST.get('email','')
        number=request.POST.get('number','')
        message=request.POST.get('message','')       
        enquer=Enquery(names=names,email=email,number=number,message=message)
        enquer.save()
    return render(request,'index.html',{"homes":homes,"testi":testi})

def about(request):
    return render(request,'about.html')

def test(request):
    return render(request,'test.html')

def package(request):
    packag=Package.objects.all()
    return render(request,'package.html',{"packag":packag})

def packages(request,id):
    pac=Package.objects.get(id=id)
    return render(request,'packages.html',{"pac":pac})

def blog(request):
    blogg=Blog.objects.all()
    return render(request,'blog.html',{"blogg":blogg})

def blogpage(request):
    blog=Blog.objects.all()
    return render(request,'blogpage.html',{"blog":blog})

def blogpages(request):
    bloggs=Blog.objects.all()
    return render(request,'blogpages.html',{"bloggs":bloggs})

def gallery(request):
    gallerys=Gallery.objects.all()
    return render(request,'gallery.html',{'gallerys':gallerys})

def branches(request):
    branchs=Branch.objects.all()
    return render(request,'branches.html',{"branchs":branchs})

def branchplace(request,id):
    branchss=Branch.objects.get(id=id)
    return render(request,'branchplace.html',{'branchss':branchss})

def contacts(request):
    contact = Contact.objects.all()
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject','') 
        message = request.POST.get('message', '')
        if not phone:
            return HttpResponse("Phone number is required")
        try:
            phone = int(phone)
        except ValueError:
            return HttpResponse("Invalid phone number")
        enq = Contact(name=name, email=email, phone=phone, subject=subject, message=message)
        enq.save()
    return render(request,'contacts.html',{'contact':contact})

def appointment(request):
    homy = Appointment.objects.all()
    if request.method == "POST":
        name = request.POST.get('names', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '') 
        time = request.POST.get('time', '')
        date = request.POST.get('date', '')
        age = request.POST.get('age', '')
        gender = request.POST.get('gender', '')
        address = request.POST.get('address', '')
        message = request.POST.get('message', '')
        if not phone:
            return HttpResponse("Phone number is required")
        try:
            phone = int(phone) 
        except ValueError:
            return HttpResponse("Invalid phone number")
        enquer = Appointment(name=name, email=email, phone=phone, date=date, time=time, age=age, gender=gender, address=address, message=message)
        enquer.save()
    return render(request, 'appointment.html', {"homy": homy})

def privacy(request):
    return render(request,'privacy.html')

def terms(request):
    return render(request,'terms.html')

def department(request):
    return render(request,'department.html')