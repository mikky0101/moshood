from unicodedata import name
from django.urls import path
from .views import home, logout_view, signup, login_view, profile, deposit, withdraw, history, deposit2, edit, faq, active, support

app_name = "main"

urlpatterns = [
    path('home/', home, name="home"),
    path('sign-up/', signup, name="sign-up"),
    path('login/', login_view, name="login"),
    path('profile/', profile, name="profile"),
    path('deposit/', deposit, name="deposit"),
    path('deposit-confirm/', deposit2, name="deposit2"),
    path('withdraw/', withdraw, name="withdraw"),
    path('history/', history, name="history"),
    path('faq/', faq, name="faq"),
    path('support/', support, name="support"),
    path('logout/', logout_view, name="logout"),
    path('active-depo/', active, name="active"),
    path('edit/', edit, name="edit")
]