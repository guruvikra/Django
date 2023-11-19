from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, render,redirect,HttpResponseRedirect
from django.contrib import admin
from newww.models import Data
from newww.models import Review,FavRest,Reviews
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.urls import path
# Create your views here.

def base(request):
    return render(request,'base.html')

def signupp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password= request.POST.get('password')
        email = request.POST.get('mail')
        phnnumber=request.POST.get('number')
        print(username,password,email,phnnumber)
        if User.objects.filter(username__iexact=username).exists():
            messages.warning(request,"username already exists")
            return redirect('signup')
        
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,"created")
        # return HttpResponse("created success")
        return redirect('signin')

    return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('signin')


    return render(request,'signin.html')

def logoutpage(req):
    logout(req)
    return redirect('base')

@login_required(login_url='signin')
def Home(request):
    data=Data.objects.all()
    # favData=FavRest.objects.filter(rest_user_name = request.user.id)
    print("Working")
    if request.method=='GET':
        st=request.GET.get('search')
        print("Working")
        if(st!=None):
            data=Data.objects.filter(rest_rating__gt=st)
            print(data)
    list={
        'data':data
    }
    return render(request,"home.html",list)
# def admin(request):
#     return render(request,);
def Index(request):
    return  render(request,"admin.html")
# def Praccc(Req,id):
#     return HttpResponse(id)
# 
@login_required(login_url='signin')
def Register(request):
    return render(request,"register.html")

@login_required(login_url='signin')
def update_review(request):
    return render(request,"updaterating.html")


# @login_required(login_url='signin')
# def Savereview(request):
#     if request.method=="POST":
        
#         name=request.POST.get('name')
#         rating=request.POST.get('rate')
#         review=request.POST.get('review')
#         rest_user_name=request.user.username
#         insert=Review(rest_name=name,rest_rating=rating,rest_review=review)
#         insert.save()
#         # print(request)
#     return render(request,"user.html")

@login_required(login_url='signin')
def Savereviews(request):
    if request.method=="POST":
        username=request.POST.get('username')
        name=request.POST.get('name')
        rating=request.POST.get('rate')
        review=request.POST.get('review')
        # rest_user_name=request.user.username
        insert=Reviews(rest_username=username,restname=name,restrating=rating,restreview=review)
        insert.save()
        # print(request)
    return render(request,"home.html") 

def updatereview(request):
    if request.method=="POST":
        username=request.POST.get('username')
        restname=request.POST.get('name')
        rating=request.POST.get('rate')
        if Reviews.objects.filter(rest_username = username,restname=restname):
            Reviews.objects.update_or_create(restrating=rating)
        else:
            insert=Reviews(rest_username=username,restname=restname,restrating=rating)
            insert.save()

    data=Data.objects.all()
    list={
        'data':data
    }
    return render(request,'home.html',list)



@login_required(login_url='signin')
def Favourite(request):
    # fav=get_object_or_404(Fav,id=id)
    # if fav.favourites.filter(id=request.user.id).exists():
    #     fav.favourites.remove(request.user)
    # else:
    #     fav.favourites.add(request.user)
    # # return redirect('home')
    # return HttpResponseRedirect(fav.get_absolute_url())
    if request.method=="POST":
        print("Working")
        rest_user_name = request.user.id
        rest_hotel_name = request.POST.get('rest_id')
        print("Working")
        insert=FavRest(rest_user_name=rest_user_name,rest_hotel_name=rest_hotel_name)
        insert.save()
        print(rest_hotel_name)
        print(rest_user_name)
    return HttpResponsePermanentRedirect("/favlist/")

@login_required(login_url='signin')
def Favlist(request):
    data=FavRest.objects.filter(rest_user_name = request.user.id)
    rest_data = []
    print(data)
    for i in data:
        print(i)
        rest_data.append(Data.objects.filter(id = i.rest_hotel_name))
    list={
        'data':rest_data
    }
    for i in list['data']:
        for j in i:
            print(j.rest_name)
    return render(request,'Favlist.html',list)

def Del(request):
    if request.method == "POST":
        rest_user_name = request.user.id    
        rest_hotel_name = request.POST.get('rest_id')
        fav = FavRest.objects.filter(rest_user_name = rest_user_name,rest_hotel_name = rest_hotel_name)
        fav.delete()
    return HttpResponsePermanentRedirect("/favlist/")