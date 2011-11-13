from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

def home(request):
    return render_to_response('base.html', context_instance=RequestContext(request))