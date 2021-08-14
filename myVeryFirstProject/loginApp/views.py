from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
from .models import Student


def index(request):
    template_name = "loginApp/show.html"
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, template_name)
        if request.method == "POST":
            items = Student.objects.create(
                name=request.POST.get('firstName'),
                address=request.POST.get('address'),
                tel_number=request.POST.get('phoneNumber'),
                email=request.POST.get('email'),
                gender=request.POST.get('gender'),
                remarks=request.POST.get('remarks'),
            )
            return render(request, template_name)
    else:
        return render(request, 'loginApp/index.html')


def delete(request):
    template_name = "dashboard/delete.html"
    if request.user.is_authenticated:
        items = Student.objects.get(pk=Student.name)
        items.delete()
        return redirect(request, template_name)
    else:
        return render(request, 'loginApp/show.html')


def update(request):
    template_name = "loginApp/update.html"
    data = Student.objects.filter(pk=Student.name)
    if data:
        data = Student.objects.get(pk=Student.name)
        image = data.image
    if request.method == "POST":
        if data:
            data.name = request.POST.get('title')
            data.address = request.POST.get('address')
            data.tel_number = request.POST.get('tel_number')
            data.email = request.POST.get('email')
            data.gender = request.POST.get('gender')
            data.image = request.FILES.get(
                'image') if request.FILES.get('image') else image
            data.save()
        return redirect(request, template_name)
    else:
        return render(request, 'loginApp/show.html')


def show(request):
    template_name = "loginApp/show.html"
    if request.user.is_authenticated:
        if request.method == "GET":
            items = Student.objects.all()
            context = {
                'items': items,
            }
            return render(request, template_name, {"data": context})
    else:
        return render(request, 'loginApp/index.html')
