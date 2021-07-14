from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


# Низкоуровневый админский интерфейс
from django.contrib.auth.admin import UserAdmin
# Register your models here.


# Создаем свой интерфейс по взаимодействию с моделью на основе UserAdmin
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "age", "username", "is_staff"]


# Регистрируем интерфейс в панель
admin.site.register(CustomUser, CustomUserAdmin)
