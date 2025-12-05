from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path('register/customer/', views.register_customer, name='register_customer'),
    path('register/driver/', views.register_driver, name='register_driver'),
    path('register/restaurant/', views.register_restaurant, name='register_restaurant'),

    path("admin-panel/", views.admin_dashboard, name="admin_dashboard"),
    path("dashboard/", views.admin_dashboard, name="dashboard"),

    path("approvals/", views.account_approvals, name="approvals"),
    path("approve/<int:user_id>/", views.approve_user, name="approve_user"),

    path("drivers/", views.manage_drivers, name="drivers"),
    path("restaurants/", views.manage_restaurants, name="restaurants"),
    path("orders/", views.manage_orders, name="orders"),
    path("chat/", views.admin_chat, name="chat"),
]
