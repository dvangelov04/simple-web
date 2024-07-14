from django.shortcuts import render, redirect
from .utils import win_lose_total, last_price, opening_prices
from .models import Stocks
from django.contrib.auth.decorators import login_required 
from .forms import StockForm
from datetime import date 


@login_required
def home(request):
    winners, losers, total = win_lose_total(request)
    stock = Stocks.objects.filter(owner=request.user).values_list('name', flat=True)
    today = date.today()
    date2day = today.strftime('%B, %d, %Y') 
    
    
    context= {
        "date":date2day,
        'stocks':stock,
        'winners':winners,
        'losers':losers,
        'total':total
    }
    
    return render(request, 'home.html', context)

@login_required
def stocks(request):
    
    if request.method == "POST":
        form = StockForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
        return redirect('stocks')
    else:
    
        stock = Stocks.objects.filter(owner=request.user).all
        id = Stocks.objects.filter(owner=request.user).values_list('id', flat=True)
        
        context = context= {
            "page_text":"Hi",
            'stocks':stock,
            'opened':opening_prices(request),
            'closed':next(last_price(request))
        }
        return render(request, 'stocks.html', context)
    
@login_required   
def edit(request, stock_id):
    
    
    if request.method == 'POST':
        stock = Stocks.objects.filter(owner=request.user).get(pk=stock_id)
        form = StockForm(request.POST or None, instance = stock)
        if form.is_valid():
            form.save()
        return redirect('stocks')
    else:
       stock = Stocks.objects.filter(owner=request.user).get(pk=stock_id)
       return render(request, 'edit.html', {'stock':stock})
   
   

   
   

    