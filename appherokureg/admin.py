from django.contrib import admin
# Register your models here.
from .models import *


class AttedeeInline(admin.TabularInline):
    model = Attendee


class RegistrationAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'company', 'role', 'email')


class WorkshopAdmin(admin.ModelAdmin):
	list_display = ('title', 'dateandtime', 'location')	
	inlines = [AttedeeInline]
	exclude = ('picture_url', )


admin.site.register(Attendee, RegistrationAdmin)
admin.site.register(Workshop, WorkshopAdmin)
