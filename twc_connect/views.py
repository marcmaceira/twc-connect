from django.shortcuts import render

def index(req):
    return render(req, 'twc_connect/index.html')