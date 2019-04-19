from django.shortcuts import render
# from django.shortcuts
# Create your views here.
def index(request):
    return  render(request,'index.html')
