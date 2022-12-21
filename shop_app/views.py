from rest_framework import filters
from rest_framework.generics import *

from .serializers import *


class TgUserCreateView(CreateAPIView):
    serializer_class = TgUserSerializer
    queryset = TgUser.objects.all()


class TgUserUpdateView(RetrieveUpdateAPIView):
    serializer_class = TgUserSerializer
    queryset = TgUser.objects.all()
    lookup_field = 'user_id'


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):

        queryset = Product.objects.all()
        cat_id = self.request.query_params.get('cat_id')
        if cat_id is not None:
            queryset = queryset.filter(prod_cat=cat_id)
        return queryset


class OrderCreateView(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class TgAdminListView(ListAPIView):
    serializer_class = TgAdminSerializer
    queryset = TgAdmin.objects.all()


