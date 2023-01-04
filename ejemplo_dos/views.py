from django.shortcuts import render

def index (request):
    return render(request,"ejemplo_dos/index.html",{})
