from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    # path('/', views)
    path('users/', views.api_get_all_users, name="all_users"),
    path('register/', views.register_user, name="register_user"),
    path('login/', obtain_auth_token, name="login_user"),
    path('users/<int:uid>/', views.api_specific_user, name="one_user")
]
