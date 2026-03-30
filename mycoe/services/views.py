from django.shortcuts import render

def report(request):
    return render(request, "services/report.html")

def pay(request):
    return render(request, "services/pay.html")

def status(request):
    return render(request, "services/status.html")