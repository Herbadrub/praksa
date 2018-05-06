from django.http import HttpResponse
from django.shortcuts import redirect, render


def home(request):
    return render(request, 'index.html')


def index_view(request):
    return render(request, 'index.html')
#

#  def logingoogle_view(request):
#    return render(request, 'test_project/login_google.html')

