from .models import CustomUser

# Заготовки интерфейса пользовательской модели
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    """
    Наш интерфейс взаимодействия с нашей CustomUser моделью
    Создание юзера
    """
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # При создании пользователя еще хотим указывать
        fields = ('username', 'email', 'age')
        # и возраст


class CustomUserChangeForm(UserChangeForm):
    """
    Наш интерфейс взаимодействия с нашей CustomUser моделью
    Редактирование юзера
    """
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        # + ('age', ) пока не будем редактировать возраст
        fields = ('username', 'email', 'age')
