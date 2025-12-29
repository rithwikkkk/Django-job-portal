from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.role = form.cleaned_data['role']
            user.profile.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})


# Create your views here.
