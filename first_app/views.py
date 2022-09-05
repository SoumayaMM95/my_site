from unittest import result
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

articles = {
    'sports':'SPORTS PAGE',
    'finance':'FINANCE PAGE',
    'politics':'POLITICS PAGE'
}
    
def news_view(request,topic):
    return HttpResponse(articles[topic])

def add_view(request, num1, num2) :
    # domain.com/first_app/num1/num2--> result
    result1 = num1 +num2
    result = f"{num1} + {num2} = {result1}"
    return HttpResponse (str(result))

# def sports_view(request):
#     # return HttpResponse("SPORTS PAGE")
#     return HttpResponse(articles['sports'])

# def finance_view(request):
#     # return HttpResponse("FINANCE PAGE")
#     return HttpResponse(articles['finance'])

