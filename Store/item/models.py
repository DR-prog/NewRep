from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=255) # Название товара
    price = models.FloatField() # Цена единицы товара
    amount = models.PositiveIntegerField() # Количество единиц товара на складе магазина
    date = models.DateTimeField(auto_now_add=True) # Дата публикации товара в сервисе
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) # Магазин-собственник товара
    def __str__(self):
        return self.title 
    def get_absolute_url(self):
        return reverse("detail_item", args=[str(self.id)])
# Create your models here.
