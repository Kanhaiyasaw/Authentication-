from django.contrib import admin
from runner.models import User_address

@admin.register(User_address)
class Listdisplay(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'address',
        'city',
    )
# Register your models here.
