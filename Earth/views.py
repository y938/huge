from django.shortcuts import render
from .form import ImageForm
from .models import Image, AllCategories
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



@login_required(login_url="login")
def index(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, "Earth/upload.html", {"form": form, "obj": obj})
   
    else:
           form = ImageForm()

    
    return render(request, "Earth/upload.html", { "form":form })


def category(request):
    ac =Image.objects.all()
    return render(request, 'Earth/index.html', {"ac": ac})


def all(request):
    ai =Image.objects.all()
    return render(request, 'Earth/all.html', {"ai": ai})

