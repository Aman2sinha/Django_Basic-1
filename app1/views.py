from django.shortcuts import render

from django.http import HttpResponse
def home(request):
    return render(request,'index.html',{'link':'http://127.0.0.1:8000/profile/'})
def profile(request):
    return render(request,'profile.html',{'link2':'http://127.0.0.1:8000/'})

def expression(request):
    a=int(request.POST['text1'])
    b=int(request.POST['text2'])
    c=a+2*b
    return render(request,'output.html',{'result':c})
