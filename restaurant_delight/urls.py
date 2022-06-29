from django.contrib import admin
from django.urls import path, include
from pages.views import home_view, about_view, dashboard_admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('dashboard/', dashboard_admin, name='dashboard'),
    path('members/',include('django.contrib.auth.urls')),
    path('members/',include('members.urls'))
]
