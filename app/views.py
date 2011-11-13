from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from models import *
import urllib

def home(request):
    return render_to_response('base.html', context_instance=RequestContext(request))

def test(request):
    return render_to_response('test.html', context_instance=RequestContext(request))

def login(request):
    return render_to_response('login.html', context_instance=RequestContext(request))

def logout(request):
    return HttpResponse('You are logged out')

def factual(request):
    bType = "carpet"
    zipCode = "08540"
    url = 'http://api.v3.factual.com/t/places.json?KEY=flUByXx9F8FQgB3tPIiam1t2Dn67cQ7r1J9rTz1r&filters='
    filter = '{\"category":{\"$search\":\"' + bType + '\"},'
    filter += ' \"postcode\":{\"$bw\":\"' + str(zipCode) + '\"}}'
    url += urllib.quote(filter)
    page = urllib.urlopen(url)
    return HttpResponse(page.read())

def signup(request):
    return render_to_response('signup.html', context_instance=RequestContext(request))

def signin(request):
    return render_to_response('signin.html', context_instance=RequestContext(request))

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
    project_list = Project.objects.all()
    return render_to_response('searchresults.html',
            {'project_list': project_list},
                              context_instance=RequestContext(request))

def projectDescription(request):
	return render_to_response('projectDescription.html',  context_instance=RequestContext(request))

def projectDescription(request):
	return render_to_response('buyInScreen.html',  context_instance=RequestContext(request))




