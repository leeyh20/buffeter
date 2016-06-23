from django.shortcuts import render

def buffet_list(request):
    return render(request, 'buffetinfo/buffet_list.html', {})
