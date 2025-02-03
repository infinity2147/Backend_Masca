from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet , lib_AdminViewSet

User_Router = DefaultRouter()
User_Router.register(r'User',UserViewSet)

lib_Admin_Router = DefaultRouter()
lib_Admin_Router.register(r'lib_Admin',lib_AdminViewSet)