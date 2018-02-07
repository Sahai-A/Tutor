from django.http import HttpResponse


def index(request):
	return HttpResponse("Hello, world. You're at the index")
	
def profile(request):
	return HttpResponse("this is the profile page")
	
