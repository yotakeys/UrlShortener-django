from django.shortcuts import redirect
from django.http import HttpResponse

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from django.contrib.auth import login
from .models import Url
# Create your views here.


class Login(LoginView):
    template_name = "login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('url')


class Register(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('url')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('url')
        return super(Register, self).get(*args, **kwargs)


class UrlList(LoginRequiredMixin, ListView):
    model = Url
    template_name = 'url_list.html'


def redirectUrl(request, shortUrl):
    return HttpResponse(shortUrl)
