
from django.contrib import admin
from .models import Store
from .forms import StoreChangeForm, StoreCreationForm
from django.contrib.auth.admin import UserAdmin 
# Register your models here.
class StoreAdmin(UserAdmin):
    add_form = StoreCreationForm
    form = StoreChangeForm
    model = Store
    list_display = ["username","email", "inn","year_open"]
admin.site.register(Store,StoreAdmin)

