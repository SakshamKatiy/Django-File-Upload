from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import FileUpload
from .forms import imgForm
# Create your views here.
def img(request):
    b=FileUpload.objects.all()
    if request.method == "POST":
        a= imgForm(request.POST,request.FILES)
        if a.is_valid():
            a.save()
            return HttpResponse('isuccessfully')
        else:
            pass
    else:
        a=imgForm()
    return render(request,'index.html' ,{'a':a,'b':b})
             
        