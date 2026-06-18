from django.shortcuts import render
from django.db.models import Q
from .models import MissingPerson


def search_people(request):
	q = request.GET.get('q', '').strip()
	results = []
	if q:
		results = MissingPerson.objects.filter(
			Q(name__icontains=q)
			| Q(last_seen_Location__icontains=q)
			| Q(description__icontains=q)
			| Q(aadhar_number__icontains=q)
		)
	return render(request, 'people/search.html', {'query': q, 'results': results})
