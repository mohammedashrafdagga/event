from django.contrib import admin
from .models import EventObj, SubEventObj
# Register your models here.


class EventObjAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['event_username', 'host',
                    'title', 'created', 'last_updated']


class SubEventObjAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['serial_subevent', 'in_event',
                    'title', 'created', 'last_updated']


admin.site.register(EventObj, EventObjAdmin)
admin.site.register(SubEventObj, SubEventObjAdmin)
