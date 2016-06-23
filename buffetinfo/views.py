from django.shortcuts import render
from django.utils import timezone
from .models import Buffet

def buffet_list(request):
	buffets = Buffet.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'buffetinfo/buffet_list.html', {'buffets' : buffets})