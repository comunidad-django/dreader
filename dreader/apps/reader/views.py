from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect

def home(request):
	return render_to_response('reader/home.html', context_instance=RequestContext(request))