
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Buffet, Review, Images
from django.forms import modelformset_factory
from .forms import BuffetForm, ReviewForm, FilterForm, ImageForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

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
        
    return render(request, 'buffetinfo/buffet_list.html', {'buffets' : buffets, 'form': form , 'search_term': ""})

#def buffet_filter_location(request, pk):
#    buffets = Buffet.objects.filter(location=pk)
#    return render(request, 'buffetinfo/buffet_list.html', { 'buffets' : buffets })

#def buffet_filter_cuisine_type(request, pk):
#    buffets = Buffet.objects.filter(cuisine_type=pk)
#    return render(request, 'buffetinfo/buffet_list.html', { 'buffets' : buffets })

def buffet_search(request, pk):
    buffets = Buffet.objects.search(pk)
    buffets = buffets.filter(published_date__lte=timezone.now()).order_by('published_date')
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

    
    return render(request, 'buffetinfo/buffet_list.html', {'buffets' : buffets, 'form': form , 'search_term': pk})

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
    buffets = Buffet.objects.filter(published_date__isnull=True, author=request.user).order_by('created_date')
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
    ImageFormSet = modelformset_factory(Images, form = ImageForm, extra = 3)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset= Images.objects.none())
        
        if form.is_valid() and formset.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.buffet = buffet
            review.save()

            for imageForm in formset.cleaned_data:
                #cleaned_data
                image = imageForm.get("image", "")
                if (image):
                    photo = Images(review=review, image= image)
                    photo.save()

            return redirect('buffetinfo.views.buffet_detail', pk=buffet.pk)

    else:        
        form = ReviewForm()
        formset = ImageFormSet(queryset= Images.objects.none())
    return render(request, 'buffetinfo/add_review_to_buffet.html', {'form': form, 'formset': formset}, context_instance = RequestContext(request))

@login_required
def review_approve(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.approve()
    return redirect('buffetinfo.views.buffet_detail', pk=review.buffet.pk)

@login_required
def review_remove(request, pk):
    review = get_object_or_404(Review, pk=pk)
    images = Images.objects.filter(review=review)
    for image in images:
        if (image):
            image.delete()

    review.delete()
    return redirect('buffetinfo.views.buffet_detail', pk=review.buffet.pk)