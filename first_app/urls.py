from django.urls import path
from . import views

# first_app/
urlpatterns = [
    # path('sports/',views.sports_view),
    # path('finance/',views.finance_view),
    path('<str:topic>/',views.news_view),
    path('<int:num1>/<int:num2>/',views.add_view)
]
