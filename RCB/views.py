from django.shortcuts import render

# Create your views here.
def rcb_captain(request):
    return render(request,'rcb_captain.html')

def rcb_team(request):
    return render(request,'rcb_team.html')