from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import SignUpForm, LoginForm

# Create your views here.
def test(request):
  return render(request, 'clothing/test.html')


class Login(LoginView):
  form_class = LoginForm
  template_name = 'clothing/login.html'


class SignUp(CreateView):
  form_class = SignUpForm
  template_name = 'clothing/Sign-Up.html'
  success_url = reverse_lazy('clothing:test')

  def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    self.object = user
    return HttpResponseRedirect(self.get_success_url())