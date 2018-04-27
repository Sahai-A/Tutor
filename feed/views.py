from django.http import HttpResponse, Http404,HttpResponseBadRequest, HttpResponseRedirect
from .models import User
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
import pdb;
	
	#pdb.set_trace() is debbugger 
	
def base(request):
	return render(request, 'feed/base.html',)
	
def index(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	return render(request, 'feed/index.html', {'user_id': user_id})
	
	
def profile(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	return render(request, 'feed/profile.html', {'user': user})
	
def new_profile(request):
	return render(request, 'feed/new_profile.html',)
	
def submit_profile(request):
	if request.POST:
		user = User.objects.create(name = request.POST.get('name',False))
		needs_help = request.POST.getlist('needs_help')
		can_help = request.POST.getlist('can_help')
		pdb.set_trace()
		for tag_name in needs_help:
			user.tag_set.create(name = tag_name, needs_help = 1, can_help = 0)
		for tag_name in can_help:
			user.tag_set.create(name = tag_name, needs_help = 0, can_help = 1)
		return redirect('/feed/' + str(user.id)) 
	else:
		return HttpResponseBadRequest()
			#if not valid - show error 
	#return render(request,'feed/submit_profile.html',{'name': request.POST.get('name',False)})
	
	#try:
	#	user = User.objects.get(pk=user_id)
	#except User.DoesNotExist:
	#	raise Http404("User does not exist")
	
	
	
	#text_output = profile_info.name + '     ' + profile_info.email
	#return HttpResponse(text_output)
