from django.urls import path
from webapp.views import main_page_view, bulls_and_cows_view

urlpatterns = [
    path('', main_page_view),
    path('bulls_and_cows/', bulls_and_cows_view)
]