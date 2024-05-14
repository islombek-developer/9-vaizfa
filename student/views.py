from django.shortcuts import render,redirect,get_list_or_404
from .models import Group,Teacher,Student,Product,Category
from .forms import CreatStudent

def home(request):
    home=Category.objects.all()
    return render(request,'home.html',context={'home':home})


def group(request):
    group=Group.objects.all()
    return render(request,'group.html',context={'group':group})

def teacher(request,g_id):
    teacher=Group.objects.get(id=g_id)
    tea=teacher.group_taught.all()
    return render(request,'teacher.html',context={'tea':tea})


def student(request,t_id):
    student=Teacher.objects.get(id=t_id)
    stu=student.groups_taught.all()
    return render(request,'student.html',context={'stu':stu})

def create(request):
    form=CreatStudent()
    if request.method == 'POST':
        form = CreatStudent(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'create.html', context={"form": form})

def update(request, id):
    student = Student.objects.get(id=id)
    form = CreatStudent(instance=student)
    if request.method == 'POST':
        form = CreatStudent(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'create.html', context={"form": form})

def delete(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/')

def products(request,p_id):
    pro=Category.objects.get(id=p_id)
    products=pro.products.all()
    return render(request,'products.html',context={'products':products})