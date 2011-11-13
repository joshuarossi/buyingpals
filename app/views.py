from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

def home(request):
    return render_to_response('base.html', context_instance=RequestContext(request))

def test(request):
    return render_to_response('test.html', context_instance=RequestContext(request))

def login(request):
    return render_to_response('login.html', context_instance=RequestContext(request))

def logout(request):
    return HttpResponse('You are logged out')

def signup(request):
    return render_to_response('signup.html', context_instance=RequestContext(request))

def comingsoon(request):
	return render_to_response('comingsoon.html',  context_instance=RequestContext(request))

def post(request):
	return render_to_response('post.html',  context_instance=RequestContext(request))

def confirm(request):
	return render_to_response('confirm.html',  context_instance=RequestContext(request))

def details(request):
	return render_to_response('details.html',  context_instance=RequestContext(request))

def providers(request):
	return render_to_response('providers.html',  context_instance=RequestContext(request))

def search(request):
	return render_to_response('search.html',  context_instance=RequestContext(request))

def searchresults(request):
	return render_to_response('searchresults.html',  context_instance=RequestContext(request))


