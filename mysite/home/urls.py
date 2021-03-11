
from django.urls import include, path
from . import views
from django.views.generic import TemplateView

app_name="home"

urlpatterns = [
    path('', views.home, name='home'),
    path('info/', views.info, name='info'),
    path('patrocinadores/', views.patrocinadores, name='patrocinadores'),
    path('preparacion/', views.preparacion, name='preparacion'),
    path('agenda/', views.agenda, name='agenda'),
    path('lookup/', views.lookup, name="lookup"),
    path('accounts/',include('django.contrib.auth.urls'), name="accounts"),
    path("logout/", views.log_user_out, name="logout"),
    path('accounts/sign_up/',views.sign_up,name="sign-up"),
]