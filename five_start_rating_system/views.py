from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import Rating



# Create your views here.
def front_page(request):
	return render(request, 'five_start_rating_system/front_page.html', {
		
		})


def process_review(request):

	if request.method == 'POST':
		rating = request.POST.get('rate')
		comment = request.POST.get('five_star_rating_comment_ta')

		r = Rating(user=request.user, rating=rating, comment=comment)
		r.save()




		return redirect('five_start_rating_system:process_review')
	
	

	return render(request, 'five_start_rating_system/five_star_rating_form.html', {
			
		})



def ratings(request):
	

	return  {
			'ratings':Rating.objects.all()
		}