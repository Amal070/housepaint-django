from django.urls import path
from . import views
urlpatterns = [

    path('user_home', views.index, name='index'),


    path('shop_home', views.shop_home, name='shop_home'),
    path('shop_register', views.shop_register, name='shop_register'),
    path('shop_login', views.shop_login, name='shop_login'),
    
    path('add_profile', views.add_profile, name='add_profile'),
    path('view_profile/<int:pk>/', views.view_profile, name='view_profile'),
    path('Update_profile/<int:pk>/', views.Update_profile, name='Update_profile'),

    path('add_worker', views.add_worker, name='add_worker'),
    path('view_worker', views.view_worker, name='view_worker'),
    path('update_worker/<int:pk>/', views.update_worker, name='update_worker'),
    path('delete_worker/<int:pk>/', views.delete_worker, name='delete_worker'),

    path('add_package', views.add_package, name='add_package'),
    path('view_package', views.view_package, name='view_package'),
    path('update_package/<int:pk>/', views.update_package, name='update_package'),
    path('delete_package/<int:pk>/', views.delete_package, name='delete_package'),

    path('view_request', views.view_request, name='view_request'),
    path('approve_request/<int:pk>/', views.approve_request, name='approve_request'),
    path('add_message/<int:pk>/', views.add_message, name='add_message'),

    path('approved_client', views.approved_client, name='approved_client'),
    path('generat_bill/<int:pk>/', views.generat_bill, name='generat_bill'),

    path('shop_SignOut', views.shop_SignOut, name='shop_SignOut'),
    
    

    ############### ### user panel start ####################

    path('', views.user_home, name='user_home'),
    path('user_register', views.user_register, name='user_register'),
    path('user_login', views.user_login, name='user_login'),

    path('add_user_profile', views.add_user_profile, name='add_user_profile'),
    path('view_user_profile/<int:pk>/', views.view_user_profile, name='view_user_profile'),
    path('Update_user_profile/<int:pk>/', views.Update_user_profile, name='Update_user_profile'),
  
    path('view_package_detils/<int:pk>/', views.view_package_detils, name='view_package_detils'),

    path('send_package_request/<int:pk>/', views.send_package_request, name='send_package_request'),

    path('success_message', views.success_message, name='success_message'),
    path('purchase_history', views.purchase_history, name='purchase_history'),

    path('view_worked', views.view_worked, name='view_worked'),

    path('view_bill', views.view_bill, name='view_bill'),

    path('client_SignOut', views.client_SignOut, name='client_SignOut'),
]