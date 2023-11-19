from django.shortcuts import render,HttpResponse

# Create your views here.
def Home(Req):
    return  HttpResponse("<h1>hello</h1>")

# def Praccc(Req,id):
#     return HttpResponse(id)
def P(request,id):
    return HttpResponse(id)
