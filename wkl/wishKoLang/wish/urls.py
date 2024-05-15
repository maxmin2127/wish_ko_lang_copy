from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.welcome, name="welcome"),
    path("login/", views.login, name="login"), 
    path("signup/", views.signup, name="signup"), 
    path("signup/setup", views.setup, name="setup"), 

    path("home/", views.home, name="home"), 
    path("openGifting/", views.openGifting, name="openGifting"), 
    path("secretSanta/", views.secretSanta, name="secretSanta"), 
    path("friends/", views.friends, name="friends"), 

    path("openGifting/organization/<int:organization_id>", views.organization, name="organization"),
    path("openGifting/organization/<int:organization_id>/<int:member_id>", views.member_clicked, name="member"),
    path("secretSanta/create", views.createGroup, name="createGroup"), 
    path("secretSanta/group",  views.group, name="group"), 
    path("secretSanta/group/runRoulette", views.runRoulette, name="runRoulette")

    
]