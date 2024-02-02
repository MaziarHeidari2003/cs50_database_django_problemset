from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('create', views.create_listing,name='create'),
    path('display_category', views.display_category, name="display_category"),
    path('listing/<int:id>',views.listing, name="listing"),
    path('remove_watch_list/<int:id>',views.remove_watch_list, name="remove_watch_list"),
    path('add_watch_list/<int:id>',views.add_watch_list, name="add_watch_list"),
    path('watch_list', views.watch_list,name='watch_list'),
    path('add_comment/<int:id>', views.add_comment,name='add_comment')
  
]
