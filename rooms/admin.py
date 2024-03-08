from django.contrib import admin

from .models import House, Room

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Room, RoomAdmin)

class HouseAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(House, HouseAdmin)