from django.db import models


class TgUser(models.Model):
    user_firstname = models.CharField(max_length=200, verbose_name='Никнейм')
    user_id = models.PositiveBigIntegerField(unique=True, null=False, verbose_name='Телеграмм айди')
    user_phone = models.CharField(max_length=20, unique=True, verbose_name='Номер')
    user_username = models.CharField(max_length=200, null=True, blank=True, verbose_name='Имя пользователья')
    user_is_referral = models.PositiveBigIntegerField(null=True, blank=True, verbose_name='Реферал')
    user_referrals_count = models.PositiveIntegerField(null=True, blank=True, default=0,
                                                       verbose_name='Количество рефералов')
    user_referrals_balance = models.PositiveIntegerField(null=True, blank=True, default=0,
                                                         verbose_name='Доход с рефералов')
    is_banned = models.BooleanField(default=False, verbose_name='Заблокировать')
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.user_username

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"


class Category(models.Model):
    cat_name = models.CharField(unique=True, blank=False, max_length=200, verbose_name='Название',
                                help_text='Введите название категории')
    cat_create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"


class Product(models.Model):
    prod_name = models.CharField(max_length=500, verbose_name='Название', help_text='Введите название товара')
    prod_cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    prod_descr = models.TextField(blank=False, help_text='Введите Описание товара', verbose_name='Описание')
    prod_photo = models.ImageField(blank=False, upload_to='photos/%Y/%m/%d/', help_text='Загрузите фото товара',
                                   verbose_name='Фото')
    prod_price = models.PositiveBigIntegerField(blank=False, default=0, help_text='Укажите цену товара',
                                                verbose_name='Цена')
    prod_quantity = models.PositiveIntegerField(blank=False, default=0, help_text='Укажите количество товара',
                                                verbose_name='Количество')
    prod_create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.prod_name

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Товары"


class Order(models.Model):
    delivery_choice_option = [
        ('Доставка', 'Доставка'),
        ('Сомавывоз', 'Сомавывоз'),
    ]

    pay_choice_option = [
        ('Наличными', 'Наличными'),
        ('Оплата в боте', 'Оплата в боте'),
    ]

    order_user = models.ForeignKey(TgUser, on_delete=models.PROTECT, verbose_name='Заказчик')
    order_delivery_type = models.CharField(choices=delivery_choice_option, max_length=10, verbose_name='Тип доставки')
    order_pay_type = models.CharField(choices=pay_choice_option, max_length=20, verbose_name='Тип оплаты')
    order_address = models.TextField(null=True, blank=True, verbose_name='Адрес ')
    order_prod = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Товар')
    order_prod_quan = models.PositiveBigIntegerField(null=False, blank=False, verbose_name='Количество')
    order_create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = "Заказы"
        verbose_name_plural = "Заказы"


class TgAdmin(models.Model):
    admin_name = models.CharField(blank=False, null=False, max_length=100, verbose_name='Имя админа')
    admin_id = models.PositiveBigIntegerField(unique=True, blank=False, null=False, verbose_name='Айди админа',
                                              help_text='⚠Прежде чем добавлять аккаунт админа убедитесь что из этого аккаунта нажали старт на бота⚠')
    admin_created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.admin_name

    class Meta:
        verbose_name = "Админы в телеграме"
        verbose_name_plural = "Админы в телеграме"