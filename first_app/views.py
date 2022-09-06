from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def simple_view(request):
    return render(request,'first_app/example.html') # .html 


# articles = {
#     'sports':'SPORTS PAGE',
#     'finance':'FINANCE PAGE',
#     'politics':'POLITICS PAGE'
# }
    
# def news_view(request,topic):
#     try:
#         result = articles[topic]
#         return HttpResponse(result)
#     except:
#         # result = 'PAGE NOT FOR THAT TOPIC'
#         # return HttpResponseNotFound(result)
#         raise Http404("404 GENERIC ERROR") # 404.html


# # domain_name.com/first_app/0 ---> domain_name.com/first_app/first_topic
# def num_page_view(request,num_page):

#     topics_list = list(articles.keys())
#     topic = topics_list[num_page]

#     # return HttpResponseRedirect(topic)

#     # webpage = reverse('topic-page', args=[topic])
#     # return HttpResponseRedirect(webpage)
#     return HttpResponseRedirect(reverse('topic-page', args=[topic]))




# def add_view(request, num1, num2) :
#     # domain.com/first_app/num1/num2--> result
#     result1 = num1 +num2
#     result = f"{num1} + {num2} = {result1}"
#     return HttpResponse (str(result))

# def sports_view(request):
#     # return HttpResponse("SPORTS PAGE")
#     return HttpResponse(articles['sports'])

# def finance_view(request):
#     # return HttpResponse("FINANCE PAGE")
#     return HttpResponse(articles['finance'])

