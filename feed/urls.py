from django.urls import path
from . import views

urlpatterns = [
	path('', views.base, name='base'),
	path('<int:user_id>', views.index, name = 'index'),	
	path('profile/<int:user_id>', views.profile, name='profile'),
	path('profile/new', views.new_profile, name='new_profile'),
	path('profile/submit-profile', views.submit_profile, name='submit_profile')
]
