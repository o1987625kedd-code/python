from django.shortcuts import render
from django.http import HttpResponse

def ticket_list(request):
  ticket_number = "T0001"
  
  if request.method == "POST":
    question = request.POST.get("question")
    category = request.POST.get("category")
    submitted = True
  else:
    submitted = False
    
  return render(request,"ticket_list.html",locals())