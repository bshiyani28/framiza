from django.shortcuts import render
from main.models import UserData
# Create your views here.
def index(request):
    name = ""
    gender = ""
    mobile = ""
    if request.method == "POST":
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        mobile = request.POST.get("mobile")
        # print(f"Name: {name}, Gender: {gender}, Mobile: {mobile}")  # Just for testing
        
    obj = UserData(
        name = name,
        gender = gender,
        mobile = mobile
    )
    
    obj.save()
    return render(request, 'index.html')