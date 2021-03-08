from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic.edit import View
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CreateUserForm
from django.contrib.auth.models import Group


def RegisterUser(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group_name = form.cleaned_data.get('position')
            group = Group.objects.get(name=group_name)
            group.user_set.add(user)
            user.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'in/registration.html', context)


class Login(View):
    form = LoginForm
    template_name = 'in/login.html'
    error = ''

    def get(self, request):
        form = self.form(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                if auth_user.is_active:
                    login(request, auth_user)
                    return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('login')
        return render(request, self.template_name, {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('login')
