from django.contrib import admin
from .models import Room, Reservation

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_night', 'description')


admin.site.register(Room, RoomAdmin)

admin.site.register(Reservation)