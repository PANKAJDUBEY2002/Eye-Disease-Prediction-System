
from BRMapp import views
from django.urls import path,re_path
from BRMapp import views
urlpatterns=[
path('view-books',views.viewBooks),
path('edit-book',views.editBook),
path('delete-book',views.deleteBook),
path('search-book',views.searchBook),
path('new-book',views.newBook),
path(r'^add',views.add),
path('BRMapp/search',views.search),
path('edit',views.edit),
path('login',views.userLogin),
path('logout',views.userLogout),
]
