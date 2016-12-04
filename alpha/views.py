from django.shortcuts import render
from .models import AlphaBoard
# Create your views here.

def index(request):
    alpha_request = AlphaBoard.objects.order_by('modified_on')

    context = {'alpha_list': alpha_request}
    return render(request, 'alpha/index.html', context)
