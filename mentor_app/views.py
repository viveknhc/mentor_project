from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    course = Course.objects.all()
    trainer = Trainer.objects.all()
    context = {
        "course":course,
        "trainer":trainer,
        "is_index":True
    }
    return render(request,"app1/index.html",context)

def about(request):
    testimonial = Testimonial.objects.all()
    context = {
        "testimonial":testimonial,
        "is_about":True
    }
    return render(request,"app1/about.html",context)



def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        sub = request.POST['subject']
        msg = request.POST['message']
        object = Contact(name=name,email=email,subject=sub,message=msg)
        object.save()
    context = {
        "is_contact":True
    }
    return render(request,"app1/contact.html",context)


def courses(request):
    course = Course.objects.all()
    context = {
        "courses":course,
        "is_courses":True
    }
    return render(request,"app1/courses.html",context)


def trainer(request):
    trainer = Trainer.objects.all()
    context = {
        "trainer":trainer,
        "is_trainer":True
    }
    return render(request,"app1/trainers.html",context)


def coursesD(request):
    return render(request,"app1/course-details.html")
def events(request):
    context = {
        "is_events":True
    }
    return render(request,"app1/events.html",context)


def price(request):
    context = {
        "is_price":True
    }
    return render(request,"app1/pricing.html",context)