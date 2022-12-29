from django.contrib import admin
from runner.models import User_address

@admin.register(User_address)# decorator for register the model
class Listdisplay(admin.ModelAdmin):# show the feilds on front of model on admin panel
    list_display = (
        'id',
        'user',
        'address',
        'city',
    )

