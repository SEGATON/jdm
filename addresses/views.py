from django.shortcuts import render

# Create your views here.


def front_page(request):
	return render(request, 'addresses/front_page.html',{})