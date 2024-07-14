from django.shortcuts import render, redirect
from .form import CustomRegistrationForm
from quote import quote

def register(request):
    
    if request.method == "POST":
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else: 
        form = CustomRegistrationForm()
        
    return render(request, 'registration.html', {'register': form})

def index(request):
    search = 'philosophy'
    result = quote(search, limit=1) 
    idk = []
    for i in result: 
        for key, value in i.items(): 
            idk.append(value)
        
    return render(request, 'index.html', {"page_text":idk})

