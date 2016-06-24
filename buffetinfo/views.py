
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Buffet

def buffet_list(request):
	buffets = Buffet.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'buffetinfo/buffet_list.html', {'buffets' : buffets})

def buffet_detail(request, pk):
    buffet = get_object_or_404(Buffet, pk=pk)
    return render(request, 'buffetinfo/buffet_detail.html', {'buffet': buffet})