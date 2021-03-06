from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from login import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('special/',views.special,name='special'),
    path('login/',include('login.urls')),
    path('logout/', views.user_logout, name='logout'),
    path('time-table/', views.time_table, name='time_table'),
    path('contest-stats/',views.contest_stats, name='contest_stats'),
    path('login/search-handle/',views.search_handle, name='search_handle'),
    
] 