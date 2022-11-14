from django.urls import path
from .views import Login, Register, UrlList
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', name='url', view=UrlList.as_view()),
    path('login', name='login', view=Login.as_view()),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register', name='register', view=Register.as_view()),
]
