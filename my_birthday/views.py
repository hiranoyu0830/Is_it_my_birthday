from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "my_birthday/index.html", {
        "my_birthday": now.month == 8 and now.day == 30
    })