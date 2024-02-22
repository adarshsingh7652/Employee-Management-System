from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from Information.models import user

# this is main page function.
def index(request):
    return render(request,"index.html")

# this is add detail function.
def form(request):
    
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        department=request.POST['department']
        position=request.POST['position']
        f=user(Name=name,Email=email,Department=department,Position=position)
        f.save()
        return HttpResponseRedirect('/employees_detail/')
    
    return render(request,"add_detail.html")
    

# this is employees detail function.
def show(request):
    fn=user.objects.all().order_by("id")
    if request.method == "POST":
        BT=request.POST['btn']
        if BT != None:
            fn=user.objects.filter(id__icontains = BT)
    data={
        "fn":fn
    }
    return render(request,"emp_detail.html",data)
#this is a delete function.
def delet(request,id):
    
        D=user.objects.get(pk=id)
        D.delete()
        return HttpResponseRedirect('/employees_detail/')
    
# this is update function.
def update(request,id):
    std=user.objects.get(pk=id)
    
    
    return render(request,"update.html",{"std":std})

def sav(request,id):
    name=request.POST['name']
    email=request.POST['email']
    department=request.POST['department']
    position=request.POST['position']
    td=user.objects.get(pk=id)
    td.Name=name
    td.Email=email
    td.Department=department
    td.Position=position
    
    td.save()
    return HttpResponseRedirect('/employees_detail/')


        
        
        
    
    
     
     
        
