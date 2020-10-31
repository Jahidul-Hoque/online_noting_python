
from django.http import HttpResponse
from django.urls import reverse
#from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponseRedirect


def index(request):
    return HttpResponseRedirect(reverse('noting:note_list'))
