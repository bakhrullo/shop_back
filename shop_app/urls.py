from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *


urlpatterns = [
    path('api/v1/user/create', TgUserCreateView.as_view()),
    path('api/v1/user/update/<int:user_id>', TgUserUpdateView.as_view()),
    path('api/v1/category/', CategoryListView.as_view()),
    path('api/v1/product/', ProductListView.as_view()),
    path('api/v1/order/', OrderCreateView.as_view()),
    path('api/v1/tgadmin/', TgAdminListView.as_view()),
]
