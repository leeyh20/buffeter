from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import AccountForm, ProfileForm
from .models import UserProfile

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

def account_profile(request):
    if (request.user.is_authenticated()):
        profile = get_object_or_404(UserProfile, user= request.user)
        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                
                profile.birth_date = form.cleaned_data["birth_date"]
                profile.gender = form.cleaned_data["gender"]
                profile.profile_pic = form.cleaned_data["profile_pic"]

                if (not profile.user):
                    profile.user = request.user

                profile.save() 
                return redirect('/')
        else:
            form = ProfileForm(instance=profile)
        return render(request, 'useradmin/account_profile.html', {'form': form, 'pic': profile.profile_pic})
    else:
        return render(request, 'useradmin/account_noprofile.html')

    