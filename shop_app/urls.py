from django.urls import path

from .views import *


urlpatterns = [
    path('api/v1/user/', TgUserListView.as_view()),
    path('api/v1/user/create', TgUserCreateView.as_view()),
    path('api/v1/user/update/<int:user_id>', TgUserUpdateView.as_view()),
    path('api/v1/category/', CategoryListView.as_view()),
    path('api/v1/product/', ProductListView.as_view()),
    path('api/v1/order/', OrderCreateView.as_view()),
    path('api/v1/tgadmin/', TgAdminListView.as_view()),
    path('api/v1/percent/', PercentGetView.as_view()),
    path('api/v1/bot/', TgBotGetCreateView.as_view()),
]
