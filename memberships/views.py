from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic
# Create your views here.

from django.http import HttpResponseRedirect
from .models import Bookmark
from .models import Profile

from django.contrib.auth.decorators import login_required

def profile(request):

	return render(request, 'memberships/profile.html', {
		
		})

class PublicProfile(generic.DetailView):
	model = Profile
	template_name = 'memberships/public_profile.html'
	object_context_name = 'profiles'

	def get_queryset(self):
		return Profile.objects.all().exclude(user=self.request.user) 
	def get_object(self, *kwargs):
		pk = self.kwargs.get('pk') 
		koko = Profile.objects.get(pk=pk)
		content = {
			'koko':koko
		}
		return content
	def get_context_data(self, *args, **kwargs):
		context = supser().get_context_data(**kwargs)

		return context

def edit_profile(request, pk):
	
	return render(request, 'memberships/edit_profile.html', {
		
		})

def delete_profile(request, pk):
	
	return render(request, 'memberships/delete_profile.html', {
		
		})

def follow_profile(request, pk):
	pass





@login_required
def bookmarks(request, pk):
	profile = get_object_or_404(Profile, pk=pk)
	
	return render(request, 'memberships/bookmarks.html' ,{
			'profile':profile
		})

@login_required
def add_to_bookmarks(request, slug):

	return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def remove_from_bookmarks(request, slug):

	return HttpResponseRedirect(request.META['HTTP_REFERER'])

























