from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=100,verbose_name='Наименование товара')
    producer = models.CharField(max_length=100, verbose_name='Производитель')
    country = models.CharField(max_length=100, verbose_name='Страна')
    cat = models.CharField(max_length=100, verbose_name='Категория', choices=(('1','куклы'),('2','машинки'),('3','лего')))
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Cart(models.Model):
    product = models.ManyToManyField(Product, verbose_name='выбранные товары')
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

class Order(models.Model):
    product = models.ManyToManyField(Product, verbose_name='выбранные товары')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='общая стоимость')
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
