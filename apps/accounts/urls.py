from apps.accounts.views.signin import Signin
from apps.accounts.views.signup import Signup
from apps.accounts.views.user import GetUser

from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('signin', Signin.as_view()),
    path('signup', Signup.as_view()),
    path('user', GetUser.as_view())
]