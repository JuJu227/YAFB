from django.contrib import admin

from .models import *

class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

class GroupAdmin(admin.ModelAdmin):
    list_display = ('group', 'type', 'description',)
    list_filter = ('type',)

class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'start_date', 'office')
    list_filter = ('start_date', 'title')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('writer', 'time_stamp', 'text',)

admin.site.register(Type, TypeAdmin)
admin.site.register(GroupProfile, GroupAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Message, MessageAdmin)
