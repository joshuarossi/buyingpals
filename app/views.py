from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

def home(request):
    return render_to_response('base.html', context_instance=RequestContext(request))

def login(request):
    return render_to_response('login.html', context_instance=RequestContext(request))

def logout(request):
    return HttpResponse('You are logged out')

def signup(request):
    return render_to_response('signup.html', context_instance=RequestContext(request))
