from django.shortcuts import render
from django.http import HttpResponse

def ticket_list(request):
  return render(request,"ticket_list.html")