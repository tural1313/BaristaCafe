from django.shortcuts import render, redirect
from django.conf.urls.static import static 
from baristaapp.models import Cafe, About, Work_Team, Menu, Reviews, Contact, Reservation, PeopleNumber, SiteSettings

def index(request):
    settings = SiteSettings.objects.first()
    cafes = Cafe.objects.all()
    abouts = About.objects.all()
    work_teams =Work_Team.objects.all()
    menus = Menu.objects.all()
    reviews = Reviews.objects.all()
    contacts = Contact.objects.all()
    
    
        
    context = {
        "settings": settings,
        "cafes": cafes,
        "abouts": abouts,
        "work_teams": work_teams,
        "menus": menus,
        "reviews": reviews,
        "contacts": contacts,
    }
    return render(request, 'index.html', context)


def reservation(request):
    settings = SiteSettings.objects.first()
    cafes = Cafe.objects.all()
    reservations = Reservation.objects.all()
    peoplenumbers = PeopleNumber.objects.all()
    
    if request.method == "POST":
    
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        number_of_people = request.POST.get("number")
        check_in_date = request.POST.get("data")
        time = request.POST.get("time")
        content = request.POST.get("message")
        image = request.Post.get("image")

        Reservation.objects.create(
            name = name,
            phone = phone,
            number_of_people = number_of_people,
            check_in_date = check_in_date,
            time = time,
            content = content,
            image = image
            
        )
        return redirect("reservation")

    context = {
        "settings" : settings,
        "cafes" : cafes,
        "reservations" : reservations,
        "peoplenumbers" : peoplenumbers,
        "name": name,
        "phone" : phone,
        "number_of_people" : number_of_people,
        "check_in_date" : check_in_date,
        "time" : time,
        "content" : content,
        "image" : image
    }

    return render(request, 'reservation.html', context) 