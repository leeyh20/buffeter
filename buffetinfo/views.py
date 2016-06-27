
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Buffet, Review
from .forms import BuffetForm, ReviewForm, FilterForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def buffet_list(request):
    #default filter
    buffets = Buffet.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == "POST":
        form = FilterForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            cuisine_type = form.cleaned_data['cuisine_type']
            if location != '': 
                buffets = buffets.filter(location=location)
                #return redirect('/filter/location/' + location + '/')
            if cuisine_type != '':
                buffets = buffets.filter(cuisine_type=cuisine_type)
                #return redirect('/filter/cuisine_type/' + cuisine_type + '/')
                #cannot filter price because price is char field now. Need to convert to float....
    else:
        form = FilterForm()
        
    return render(request, 'buffetinfo/buffet_list.html', {'buffets' : buffets, 'form': form })

#def buffet_filter_location(request, pk):
#    buffets = Buffet.objects.filter(location=pk)
#    return render(request, 'buffetinfo/buffet_list.html', { 'buffets' : buffets })

#def buffet_filter_cuisine_type(request, pk):
#    buffets = Buffet.objects.filter(cuisine_type=pk)
#    return render(request, 'buffetinfo/buffet_list.html', { 'buffets' : buffets })

def buffet_detail(request, pk):
    buffet = get_object_or_404(Buffet, pk=pk)
    return render(request, 'buffetinfo/buffet_detail.html', {'buffet': buffet })

@login_required
def buffet_new(request):
    if request.method == "POST":
        form = BuffetForm(request.POST)
        if form.is_valid():
            buffet = form.save(commit=False)
            buffet.author = request.user
            buffet.rating = 0.0
            #buffet.published_date = timezone.now()
            buffet.save()
            return redirect('buffet_detail', pk=buffet.pk)
    else:
        form = BuffetForm()
    return render(request, 'buffetinfo/buffet_edit.html', {'form': form})

@login_required
def buffet_edit(request, pk):
    buffet = get_object_or_404(Buffet, pk=pk)
    if request.method == "POST":
        form = BuffetForm(request.POST, instance=buffet)
        if form.is_valid():
            buffet = form.save(commit=False)
            buffet.author = request.user
            buffet.rating = 0.0
            #buffet.published_date = timezone.now()
            buffet.save()
            return redirect('buffet_detail', pk=buffet.pk)
    else:
        form = BuffetForm(instance=buffet)
    return render(request, 'buffetinfo/buffet_edit.html', {'form': form})

@login_required
def buffet_draft_list(request):
    buffets = Buffet.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'buffetinfo/buffet_draft_list.html', {'buffets': buffets})

@login_required
def buffet_publish(request, pk):
    buffet = get_object_or_404(Buffet, pk=pk)
    buffet.publish()
    return redirect('buffetinfo.views.buffet_detail', pk=pk)

@login_required
def buffet_remove(request, pk):
    buffet = get_object_or_404(Buffet, pk=pk)
    buffet.delete()
    return redirect('buffetinfo.views.buffet_list')

@login_required
def add_review_to_buffet(request, pk):
    buffet = get_object_or_404(Buffet, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.buffet = buffet
            review.save()
            return redirect('buffetinfo.views.buffet_detail', pk=buffet.pk)
    else:
        form = ReviewForm()
    return render(request, 'buffetinfo/add_review_to_buffet.html', {'form': form})

@login_required
def review_approve(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.approve()
    return redirect('buffetinfo.views.buffet_detail', pk=review.buffet.pk)

@login_required
def review_remove(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return redirect('buffetinfo.views.buffet_detail', pk=review.buffet.pk)