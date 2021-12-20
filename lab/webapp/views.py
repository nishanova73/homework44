from django.shortcuts import render

import random

def getDigits(num):
    return [int(i) for i in str(num)]

def noDuplicates(num):
    num_li = getDigits(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False

def generateNum():
    while True:
        num = random.randint(1000,9999)
        if noDuplicates(num):
            return num

FIRST_TIME = True
COMPUTER = None
HISTORY = []

# Create your views here.
def main_page_view(request):
    return render(request, 'main_page.html')

def bulls_and_cows_view(request):
    return render(request, 'bulls_and_cows.html')

def results_page_view(request):
    return render(request, 'results_page.html')