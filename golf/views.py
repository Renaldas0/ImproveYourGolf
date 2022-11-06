import datetime
from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic


def main_page(request):
    return render(request, 'golf/index.html')