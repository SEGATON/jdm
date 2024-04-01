from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect

# Create your views here.
from .forms import AddPersonForm
from .forms import EditPersonForm
from .models import Person

def front_page(request):

	return render(request, 'django_experiments_app/front_page.html', {

		})

	
def persons(request):
	persons = Person.objects.all()
	return render(request, 'persons/persons.html', {
				'persons':persons
		})
def person(request, pk):
	person = get_object_or_404(Person, pk=pk)
	return render(request, 'persons/person.html', {
				'person':person
		})

def add_person(request):

	if request.method == 'POST':
		add_person_form = AddPersonForm(request.POST)
		if add_person_form.is_valid():
			add_person_form.save()
			return redirect('django_experiments_app:persons')
	else:
		add_person_form = AddPersonForm()
	return render(request, 'forms/add_person.html', {
			'add_person_form':add_person_form
		})

def edit_person(request, pk):
	if request.method == 'POST':
		instance = get_object_or_404(Person, pk=pk)
		edit_person_form = EditPersonForm(request.POST, instance=instance)
		if edit_person_form.is_valid():
			edit_person_form.instance
			edit_person_form.save()
			return redirect('django_experiments_app:persons')
	else:
		edit_person_form = EditPersonForm()
	return render(request, 'forms/edit_person.html', {
			'edit_person_form':edit_person_form
		})

def delete_person(request, pk):
	person = get_object_or_404(Person, pk=pk)
	person.delete()

	return HttpResponseRedirect(request.META['HTTP_REFERER'])



def recipe_maker(request):
	return render(request, 'django_experiments_app/recipe_maker.html', {
		
		})