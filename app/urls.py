from django.urls import path
from .views import Login, Register, UrlList, redirectUrl, UpdateUrl, DeleteUrl
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', name='url', view=UrlList.as_view()),
    path('login/', name='login', view=Login.as_view()),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', name='register', view=Register.as_view()),
    path('url/<str:shortUrl>/', name='urlRedirect', view=redirectUrl),
    path('update/<str:pk>/', name="urlUpdate", view=UpdateUrl.as_view()),
    path('delete/<str:pk>/', name="urlDelete", view=DeleteUrl.as_view()),
]
