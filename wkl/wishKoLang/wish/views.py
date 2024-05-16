from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . models import *

from rest_framework.decorators import api_view

username = ""


# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

def welcome(request):
    return render(request, "wish/subpages/Initials/welcome.html")

@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        return render(request, "wish/subpages/Initials/login.html")
    elif request.method == 'POST':
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            account = User.objects.get(username=username) # user found, check to see
            if account.password == password:
                return render(request, "wish/pages/home.html", {"user":account})
            else:
                error_message = 'Incorrect password'
            return render(request, "wish/subpages/Initials/login.html", {'error_message': error_message})
        except User.DoesNotExist:
            error_message = 'User does not exist'
            return render(request, "wish/subpages/Initials/login.html", {'error_message': error_message})

@api_view(['GET', 'POST'])
def signup(request):
    if request.method == 'GET':
        return render(request, "wish/subpages/Initials/signup.html")
    elif request.method == 'POST':
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirmPassword = request.POST.get("confirmPassword")            
        if password != confirmPassword:
            error_message = 'Confirm password does not match'
            return render(request, "wish/subpages/Initials/signup.html", {'error_message': error_message})
        if User.objects.filter(username=username).count():
            error_message = 'User already exists'
            return render(request, "wish/subpages/Initials/signup.html", {'error_message': error_message})
        registered = User(username=username, password=password)
        registered.save()
        return render(request, "wish/subpages/Initials/setup.html", {"id":registered.id, "username":registered.username})

@api_view(['GET', 'POST'])
def setup(request):
    if request.method == 'GET':
        return render(request, "wish/subpages/Initials/setup.html")
    if request.method == 'POST':
        id = request.POST.get("id")
        username = request.POST.get("username")
        profilePicture = request.POST.get("profilePicture")
        birthday = request.POST.get("birthday")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        emailaddress = request.POST.get("emailaddress")
        bio = request.POST.get("bio")
        try:
            account = User.objects.get(id=id) # user found, check to see
            account.profile_picture_link = profilePicture
            account.birthday = birthday
            account.first_name = firstname
            account.last_name = lastname
            account.email = emailaddress
            account.bio = bio
            account.save()

            wishlist =  Wishlist(owner=account, title="My Wishlist")
            wishlist.save()
            return render(request, "wish/pages/home.html", {"user":account})
        except User.DoesNotExist:
            error_message = 'User does not exist'
            return render(request, "wish/subpages/Initials/setup", {'error_message': error_message})

def home(request):
    user = User.objects.get(username=username), 
    wishlist = Wishlist.objects.get(owner=user)
    # user = User.objects.get(username)
    return render(request, "wish/pages/home.html", {
        "user" : user, 
        "wishlist": wishlist, 
        "wishlist_items": wishlist.item_in_wishlist.all()
    })
    # wishlist = Wishlist.objects.get(owner=user)
    # return render(request, "wish/pages/home.html", {
    #     "user": user, 
    #     "wishlist": wishlist,
    #     "wishlist_items" : wishlist.item_in_wishlist.all()
    # })

# def addItem(request):
#     user = User.objects.get(username=username)
#     wishlist = Wishlist.objects.get(owner=user)



def home(request):
    user = User.objects.get(username=username), 
    wishlist = Wishlist.objects.get(owner=user)
    # user = User.objects.get(username)
    return render(request, "wish/pages/home.html", {
        "user" : user, 
        "wishlist": wishlist, 
        "wishlist_items": wishlist.item_in_wishlist.all()
    })




# def addItem(request):
#     user = User.objects.get(username=username)
#     wishlist = Wishlist.objects.get(owner=user)
#     if request.method == 'POST':
#         user = User.objects.get(username=username)
#         wishlist = Wishlist.objects.get(owner=user)
#         item_name = request.POST.get("item")
#         item_to_add = Item(item_name=item_name, wishlist=wishlist)
#         item_to_add.save()
#         wishlist.item_in_wishlist.add(item_to_add)
#         return redirect('home')
#     else:
#         return HttpResponse("Invalid Request")
  
# def deleteItem(request, item_id):
#     if request.method == "POST":
#         try:
#             instance = Item.objects.get(id=item_id)
#             instance.delete()
#             return redirect("home")
#         except Item.DoesNotExist:
#             return HttpResponse("Item does not exist.")
      
#     else:
#         return HttpResponse("Invalid Request")



def openGifting(request):
    context = {
        "organizations" : Organization.objects.all()
    }
    return render(request, "wish/pages/openGifting.html", context)

def organization(request, organization_id):
    # listing = Listing.objects.get(id = listing_id)
    organization = Organization.objects.get(id = organization_id)
    context = {
        "org" : organization, 
        "members": organization.categorizing.all()
    }
    return render(request, "wish/subpages/OpenGifting/organization.html", context)

def member_clicked(request, organization_id, member_id):
    organization = Organization.objects.get(id = organization_id)
    member = Organization_Member.objects.get(id = member_id)

    context = {
        "org" : organization, 
        "members": organization.categorizing.all(), 
        "clicked": True,
        "member": member
    }

    return render(request, "wish/subpages/OpenGifting/organization.html", context)

def secretSanta(request):
    return render(request, "wish/pages/secretSanta.html")

def createGroup(request):
    return render(request, "wish/subpages/SecretSanta/createGroup.html")

def group(request):
    return render(request, "wish/subpages/SecretSanta/group.html")

def runRoulette(request):
    return render(request, "wish/subpages/SecretSanta/runRoulette.html")

def friends(request):
    return render(request, "wish/pages/friends.html");

