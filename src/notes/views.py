from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required()
def home(request):
    print('home')
    return render(request, 'notes/home.html')

def add_note(request):
    print('add_note')


def register(request):
    print('start', request.POST)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            print('not valid')
            print('error', form.errors)
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'notes/register.html', context)
