from django.conf.urls import url
from wards_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    url(r"^$", views.ProjectList.as_view(), name="project_list"),
    url(r"^project/(?P<pk>\d+)$", views.ProjectDetail.as_view(), name="project_detail"),
    url(r"^project/(?P<pk>\d+)/update/$", views.ProjectUpdate.as_view(), name="project_update"),
    url(r"^project/(?P<pk>\d+)/delete/$", views.ProjectDelete.as_view(), name="project_delete"),
    url(r"^project/(?P<pk>\d+)/review/new/$", views.review_project, name="project_review"),
    url(r"^project/(?P<pk>\d+)/review/delete/$", views.delete_review, name="project_review_delete"),
    url(r"^project/new/$", views.ProjectCreate.as_view(), name="project_create"),
    url(r"^profile/(?P<pk>\d+)$", views.UserDetail.as_view(), name="user_detail"),
    url(r"^profile/(?P<pk>\d+)/update/$", views.update_profile, name="profile_update"),
    url(r"^about/$", views.AboutView.as_view(), name="about"),
    url(r"^search/", views.search_results, name='search_results'),

    url(r'^api/projects/$', views.ProjectListView.as_view()),
    url(r'^api/users/$', views.UserListView.as_view()),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
