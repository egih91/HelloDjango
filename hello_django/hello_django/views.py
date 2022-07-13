from django.http import HttpResponse
from django.shortcuts import render

def about (reqest):
    return  render(reqest,'about.html', {'gree':'bfjjjdjfjk'})

def home (request):
    return  HttpResponse('It is home page')