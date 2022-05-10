from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    # path('/', views)
    path('users/', views.api_get_all_users, name="all_users"),
    path('register/', views.register_user, name="register_user"),
    # path('login/', obtain_auth_token, name="login_user"),
    path('users/<str:username>/', views.api_specific_user, name="one_user"),
    path('requests/new-request/', views.new_move_request, name="new_move_request"),
    path('requests/<str:username>', views.api_get_all_users_requests, name="users_requests"),
    path('requests/', views.api_get_all_requests, name="all_requests"),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
]
