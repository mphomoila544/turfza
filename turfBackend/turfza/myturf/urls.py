from django.urls import path
from . import views
from .views import RegisterApiView, UserDetailAPI, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("", views.post),
    path("verifier", views.verifier),
    path("register", views.register),
    path("Login", views.Login),
    path("Register", RegisterApiView.as_view()),
    path("get-details", UserDetailAPI.as_view()),
    path("token/", MyTokenObtainPairView.as_view(), name="token"),
    path("token/refresh", TokenRefreshView.as_view(), name="refresh"),
    path('postPics', views.postPics, name="postPics"),
    path("detail", views.accommodationDetails, name="details"),
    path('post-rule', views.postRule, name="post-rule"),
    path('get-rule', views.getRules, name='get-rule')

]
