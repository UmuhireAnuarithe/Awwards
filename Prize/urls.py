from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^new/profile$', views.new_profile, name='new-profile'),
    url(r'^profile/$',views.profile,name = 'profile'),
    url(r'^search/', views.search_projects, name='search_projects')
]