from django.contrib import admin
from .models import Room, Reservation, Contact

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_night', 'description')


admin.site.register(Room, RoomAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ( 'id','guest_name', 'guest_email','check_out', "check_in")
admin.site.register(Reservation, ReservationAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','phone','company','subject','question') 

admin.site.register(Contact, ContactAdmin)