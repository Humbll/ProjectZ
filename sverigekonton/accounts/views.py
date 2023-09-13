from django.shortcuts import render, redirect
from .forms import AccountRegistrationForm

def register_account(request):
    if request.method == 'POST':
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_created')
    else:
        form = AccountRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

def account_created(request):
    return render(request, 'accounts/account_created.html')