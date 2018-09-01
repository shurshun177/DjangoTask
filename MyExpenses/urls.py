from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^expenses/list/$', views.expense_list, name='expense_list'),
    url(r'^delete/(?P<pk>\d+)/$', views.ExpenseDelete.as_view(),
        name='expense_delete'),
    url(r'^expense/new/$', views.expense_new, name='expense_new'),
    url(r'^expense/(?P<pk>\d+)/$', views.expense_detail, name='expense_detail'),
    url(r'^expense/(?P<pk>\d+)/edit/$', views.expense_edit, name='expense_edit'),
    url(r'^expense/(?P<pk>\d+)/note/new$', views.note_new, name='note_new')
]