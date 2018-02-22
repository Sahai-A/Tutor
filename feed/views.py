from django.http import HttpResponse, Http404
from .models import User
from django.shortcuts import get_object_or_404, render

def index(request, user_id):
	return render(request, 'feed/index.html', {'user_id': user_id})
	
	
def profile(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	return render(request, 'feed/profile.html', {'user': user})
	#try:
	#	user = User.objects.get(pk=user_id)
	#except User.DoesNotExist:
	#	raise Http404("User does not exist")
	
	
	
	#text_output = profile_info.name + '     ' + profile_info.email
	#return HttpResponse(text_output)
