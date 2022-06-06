from django.shortcuts import render
from .models import familia
# Create your views here.
def familia(request):
    familia_list = familia.objects.all()
    return render (request, 'familia.html', ('familia', familia_list))

