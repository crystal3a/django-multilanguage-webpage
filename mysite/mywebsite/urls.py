from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'login', views.LoginView.as_view(), name='login'),
    url(r'logout', views.LogoutView.as_view(), name='logout'),
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    url(r'dashboard', views.DashboardView.as_view(), name='dashboard'),
    url(r'^autocomplete/newuser/$', views.AutoCompleteView.as_view(), name='autocomplete'),
]
