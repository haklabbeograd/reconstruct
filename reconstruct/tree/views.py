from django.http import HttpResponse, Http404
from django.template.loader import get_template, Context
from django.shortcuts import render_to_response, get_object_or_404

from reconstruct.tree.models import Family



def home(request):
	t = get_template("home.html")
	c = Context({'name': 'Homer i nemirno More'})
	return HttpResponse(t.render(c))



def families(request):
	families = Family.objects.all()
	return render_to_response("families.html", {'families': families})



def show_family(request, family_id):
	family = get_object_or_404(Family, pk=family_id)

	# get_object_or_404 is basicaly this:
	# try:
	# 	family = Family.objects.get(pk=family_id)
	# except Family.DoesNotExist:
	# 	raise Http404

	return render_to_response("family.html", {'family': family})
