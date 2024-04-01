from django.shortcuts import render
from .models import Vendor
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect

def front_page(request):
	vendors = Vendor.objects.all()

	return render(request, 'vendors/front_page.html', {

			'vendors':vendors

		})

@login_required
def vendor_profile(request, pk):

	vendor_profile = get_object_or_404(Vendor, pk=pk)

	return render(request, 'vendors/vendor_profile.html', {

			'vendor_profile':vendor_profile

		})

@login_required
def save_vendor(request, pk):

	return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def follow_vendor(request, pk):
	
	return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def set_notifications_from_vendor(request, pk):
	
	return HttpResponseRedirect(request.META['HTTP_REFERER'])