
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Buffet
from .forms import BuffetForm
from django.shortcuts import redirect

def buffet_list(request):
	buffets = Buffet.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'buffetinfo/buffet_list.html', {'buffets' : buffets})

def buffet_detail(request, pk):
    buffet = get_object_or_404(Buffet, pk=pk)
    return render(request, 'buffetinfo/buffet_detail.html', {'buffet': buffet})

def buffet_new(request):
    if request.method == "POST":
        form = BuffetForm(request.POST)
        if form.is_valid():
            buffet = form.save(commit=False)
            buffet.author = request.user
            buffet.rating = 0.0
            buffet.published_date = timezone.now()
            buffet.save()
            return redirect('buffet_detail', pk=buffet.pk)
    else:
        form = BuffetForm()
    return render(request, 'buffetinfo/buffet_edit.html', {'form': form})