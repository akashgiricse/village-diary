from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import Diary, dataEntryEmployee
from .forms import dataEntryForm, UserLoginForm, RegistrationForm


# Create your views here.

@login_required()
def dataEntryView(request):
    form = dataEntryForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user.username
        instance.uniqueId = form.cleaned_data["villageCode"] + "-" + form.cleaned_data["shreni"] + "-" + str(form.cleaned_data["gataNumber"])
        instance.save()
        return redirect("/dataEntry")

    context = {
        "form": form,
    }
    return render(request, "dataEntry.html", context)


def loginView(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/dataEntry')
    return render(request, 'login.html', {"form": form})


def registerView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if dataEntryEmployee.objects.filter(employeeCode=username).count()>0:
                form.save()
                return redirect('/login')
            else:
                return redirect('/register')
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'quiz/registration.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('/')