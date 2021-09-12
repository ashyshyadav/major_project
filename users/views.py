from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib import messages 
# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST) 
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('welcome')
        context = {
            'register_form':register_form
        }
        return render(request, 'users/register.html', context)
    else :
        register_form = UserRegisterForm()
        context = {
            'register_form':register_form
        }
        return render(request, 'users/register.html', context)    