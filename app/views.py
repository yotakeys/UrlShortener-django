from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView, UpdateView, DeleteView, CreateView
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
    context_object_name = 'urls'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['urls'] = context['urls'].filter(user=self.request.user)
        context['count'] = context['urls'].count()

        search = self.request.GET.get('search')
        if search:
            context['urls'] = context['urls'].filter(
                title__icontains=search)
        context['search_value'] = search
        return context


def redirectUrl(request, shortUrl):
    newLink = get_object_or_404(Url, pk=shortUrl).longUrl
    return redirect(newLink)


class UpdateUrl(LoginRequiredMixin, UserPassesTestMixin, UpdateView, ListView):
    model = Url
    fields = ['longUrl']
    template_name = "url_update.html"
    success_url = reverse_lazy('url')
    context_object_name = "urls"

    def test_func(self):
        return str(self.request.user.get_username()) == str(self.get_object().user)


class DeleteUrl(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Url
    context_object_name = 'url'
    success_url = reverse_lazy('url')
    template_name = 'url_delete.html'

    def test_func(self):
        return str(self.request.user.get_username()) == str(self.get_object().user)


class CreateUrl(LoginRequiredMixin, CreateView):
    model = Url
    fields = ['longUrl', 'shortUrl']
    success_url = reverse_lazy('url')
    template_name = 'url_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateUrl, self).form_valid(form)
