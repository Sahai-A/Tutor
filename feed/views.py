from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import User
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
import pdb;
	
def index(request, user_id):
	return render(request, 'feed/index.html', {'user_id': user_id})
	
	
def profile(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	return render(request, 'feed/profile.html', {'user': user})
	
def new_profile(request):
	return render(request, 'feed/new_profile.html',)
	
def submit_profile(request):

	if request.POST:
		user = User.objects.create(name = request.POST.get('name',False))
		pdb.set_trace()
		#if (user.is_valid()):
			#user.save()
		return redirect('/feed/' + user.id) #must be string not int, "TypeError at /feed/profile/submit-profile"
			#if not valid - show error 
	#return render(request,'feed/submit_profile.html',{'name': request.POST.get('name',False)})
	
	#try:
	#	user = User.objects.get(pk=user_id)
	#except User.DoesNotExist:
	#	raise Http404("User does not exist")
	
	
	
	#text_output = profile_info.name + '     ' + profile_info.email
	#return HttpResponse(text_output)
