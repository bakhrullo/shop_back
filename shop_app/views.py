from rest_framework.generics import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .serializers import *


class TgUserPaginate(PageNumberPagination):
    page_size = 100
    page_query_param = 'page_size'
    max_page_size = 100


class TgUserCreateView(CreateAPIView):
    serializer_class = TgUserSerializer
    queryset = TgUser.objects.all()
    # permission_classes = [IsAuthenticated]


class TgBotGetCreateView(ListCreateAPIView):
    serializer_class = TgBotSerializer
    # queryset = TgBot.objects.all()
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = TgBot.objects.all().order_by('-id')[:1]
        return queryset


class PercentGetView(ListAPIView):
    serializer_class = PercentSerializer
    queryset = Percent.objects.all()
    # permission_classes = [IsAuthenticated]


class TgUserListView(ListAPIView):
    serializer_class = TgUserListSerializer
    queryset = TgUser.objects.all()
    pagination_class = TgUserPaginate
    # permission_classes = [IsAuthenticated]


class TgUserUpdateView(RetrieveUpdateAPIView):
    serializer_class = TgUserSerializer

    lookup_field = 'user_id'
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.kwargs['user_id']
        if self.request.query_params.get('count'):
            edit_user = TgUser.objects.get(user_id=user)
            edit_user.user_referrals_count += 1
            edit_user.save()
            queryset = TgUser.objects.filter(user_id=user)
            return queryset
        elif self.request.query_params.get('price'):
            edit_user = TgUser.objects.get(user_id=user)
            print(self.request.query_params.get('price'))
            edit_user.user_referrals_balance += int(self.request.query_params.get('price'))
            edit_user.save()
            queryset = TgUser.objects.filter(user_id=user)
            return queryset
        queryset = TgUser.objects.filter(user_id=user)
        return queryset


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # permission_classes = [IsAuthenticated]


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):

        if self.request.query_params.get('prod_id'):
            prod_id = self.request.query_params.get('prod_id')
            queryset = Product.objects.all()
            if prod_id is not None:
                queryset = queryset.filter(id=prod_id)
            return queryset
        queryset = Product.objects.all()
        cat_id = self.request.query_params.get('cat_id')
        if cat_id is not None:
            queryset = queryset.filter(prod_cat=cat_id)

        return queryset


class OrderCreateView(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    # permission_classes = [IsAuthenticated]


class TgAdminListView(ListAPIView):
    serializer_class = TgAdminSerializer
    queryset = TgAdmin.objects.all()
    # permission_classes = [IsAuthenticated]
