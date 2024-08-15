from django.shortcuts import render
from .models import Login
# Create your views here.

def index (request):
    return render(request, 'pages/index.html')
def about(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        data = Login(username=user_name, password=password)
        if user_name !='' and password !='':
            data.save()
        else:
            print('!!!!!')
    return render(request, 'pages/about.html')
    