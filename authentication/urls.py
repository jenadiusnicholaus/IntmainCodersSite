from django.urls import path

from authentication.views import SignUpView, validate_username

urlpatterns = [
    path('signUp', SignUpView, name='signUp'),
    path('validate_username', validate_username, name='validate_username')
]
