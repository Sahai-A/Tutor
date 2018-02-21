from django.http import HttpResponse, Http404
from .models import User
from django.shortcuts import render

def index(request):
	return HttpResponse("Hello, world. You're at the index")
	
def profile(request):
	try:
		user = User.objects.get(pk=1)
	except User.DoesNotExist:
		raise Http404("User does not exist")
	return render(request, 'feed/index.html', {'user': user})
	
	
	#text_output = profile_info.name + '     ' + profile_info.email
	#return HttpResponse(text_output)
