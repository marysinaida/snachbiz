from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def prodcts(request):
    return render(request,'product.html')

def search_results(request):
    if 'seller' in request.GET and request.GET["seller"]:
        search_term = request.GET.get("seller")
        search_seller = Seller.objects.filter(search_term)

        message = f"{search_term}"
        
        return render(request,'search.html'{'message':message,'seller':seller})

        else:
            message = "You haven't searched for any seller"
            return render(request,'search.html'{"message":message})
