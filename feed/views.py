from django.http import HttpResponse
from .models import User


def index(request):
	return HttpResponse("Hello, world. You're at the index")
	
def profile(request):
	profile_info = User.objects.get(pk=1)
	text_output = profile_info.name + '     ' + profile_info.email
	return HttpResponse(text_output)
