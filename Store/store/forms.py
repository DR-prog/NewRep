from .models import Store
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
class StoreCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Store
        fields = ('username', 'email', 'inn')
class StoreChangeForm(UserChangeForm): 
    class Meta(UserChangeForm.Meta):
        model = Store
        fields =  ('username', 'email', 'inn')