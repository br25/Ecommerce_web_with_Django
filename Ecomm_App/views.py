from django.http import HttpResponse
from django.shortcuts import render
from .models import TestDB


def index(request):
    test = TestDB.objects.all()
    context = {
        "test":test
    }
    return render(request, "index.html", context)

