from django.shortcuts import render

# Create your views here.
def main_page_view(request):
    return render(request, 'main_page.html')

def bulls_and_cows_view(request):
    return render(request, 'bulls_and_cows.html')