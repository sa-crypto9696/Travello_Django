from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def home(request):
#     return HttpResponse("hello world")


# for adding any page 
 
# def home(request):
#     return render(request,'home.html')

# for dynamic changes in page

def home(request):
    return render(request,'home.html',{'name':'Django'})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2

    return render(request, "result.html", {'result' : res})    