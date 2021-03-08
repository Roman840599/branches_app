from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^branches/$', views.BranchList.as_view(), name=views.BranchList.name),
    url(r'^branches/(?P<pk>[0-9]+)$', views.BranchDetail.as_view(), name=views.BranchDetail.name),
    url(r'^branches/lat=(?P<lat>[+-]\d{1,3}\.\d+)&lng=(?P<lng>[+-]\d{1,3}\.\d+)$',
        views.ClothestBranchList.as_view()),
    url(r'^employees/$', views.EmployeeList.as_view(), name=views.EmployeeList.name),
    url(r'^employees/(?P<pk>[0-9]+)$', views.EmployeeDetail.as_view(), name=views.EmployeeDetail.name),
    url(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]