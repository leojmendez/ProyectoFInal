from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from ProfileAdmin.forms import FormRegisterUser, FormUserEdition, FormChangePassword

# Create your views here.
class LoginPage(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('Home')

    def get_success_url(self):
        return reverse_lazy('Home')
    
class PageRegister(FormView):
    template_name = 'register.html'
    form_class = FormRegisterUser
    redirect_autheticated_user = True
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(PageRegister, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('Home')
        return super(PageRegister, self).get(*args, **kwargs)

class UserEdition(UpdateView):
    form_class = FormUserEdition
    template_name= 'profileEdition.html'
    success_url = reverse_lazy('Home')

    def get_object(self):
        return self.request.user
    
class ChangePassword(PasswordChangeView):
    form_class = FormChangePassword
    template_name = 'changePassword.html'
    success_url = reverse_lazy('passwordSucces')

def password_succes(request):
    return render(request, 'passwordSucces.html', {})