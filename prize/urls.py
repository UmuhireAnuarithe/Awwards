from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^new/profile$', views.new_profile, name='new-profile'),
    # url(r'^projects/$',views.user_projects,name = 'user_projects'),
    url(r'^profile/$',views.profile,name = 'profile'),
    url(r'^accounts/edit-profile/', views.edit_profile, name = 'edit-profile'),
    url(r'^search/', views.search_projects, name='search_projects'),
    url(r'^api/profile/$', views.ProfileList.as_view(),name='ProfileAPI'),
    url(r'^api/projects/$', views.ProjectList.as_view(),name='ProjectAPI')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)