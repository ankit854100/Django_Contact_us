from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    # context = {
    #     "name": "Ankit Anand"
    # }
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")
    # return HttpResponse("This is About us")

def services(request):
    return render(request, "services.html")
    # return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("mobile")
        desc = request.POST.get("desc")
        contact = Contact(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, "Your data has been stored.")
    return render(request, "contact.html")