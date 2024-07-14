import yfinance as yf 
from .models import Stocks


def win_lose_total(request):
    stock = Stocks.objects.filter(owner=request.user).values_list('name', flat=True)
    number = Stocks.objects.filter(owner=request.user).values_list('number', flat=True)
    price = Stocks.objects.filter(owner=request.user).values_list('price', flat=True)
    win = []
    lose = []
    total = 0 
    
    for i in range(len(stock)): 
        ticker = yf.Ticker(str(stock[i])).history(period='1y')
        closed_price = ticker.iloc[-1].Close
        opened_price = ticker.iloc[-1].Open 
        if opened_price > closed_price: 
            lose.append(str(stock[i]))
        else:
            win.append(str(stock[i]))
        
        total += ((number[i]*closed_price) - (number[i]*price[i]))
    return win, lose, total
    
    

def last_price(request):
    stock = Stocks.objects.filter(owner=request.user).values_list('name', flat=True)
    closed = []
    while True:
        closed.clear()
        for i in range(len(stock)):
            
            ticker = yf.Ticker(str(stock[i])).history(period='1y')
            closed_price = ticker.iloc[-1].Close
            closed.append(closed_price)
        yield closed
            
def opening_prices(request):
    stock = Stocks.objects.filter(owner=request.user).values_list('name', flat=True)
    opened = []
    for i in range(len(stock)):
        ticker = yf.Ticker(str(stock[i])).history(period='1y')
        opened_price = ticker.iloc[-1].Open
        opened.append(opened_price)
    return opened
            
    

        




