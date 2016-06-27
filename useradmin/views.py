from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import AccountForm

def account_new(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            #account = form.save(commit=False)
            user_name = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(user_name, email, password)
            #buffet.published_date = timezone.now()
            user.save()
            return redirect('/accounts/login/')
    else:
        form = AccountForm()
    return render(request, 'useradmin/account_new.html', {'form': form})