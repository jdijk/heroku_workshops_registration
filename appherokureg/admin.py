from django.contrib import admin
# Register your models here.
from .models import *


class AttedeeInline(admin.TabularInline):
    model = Attendee


class RegistrationAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'company', 'role', 'email')


class WorkshopAdmin(admin.ModelAdmin):
	list_display = ('title', 'dateandtime', 'location', 'show_url')		
	inlines = [AttedeeInline]
	exclude = ('picture_url', )

	def show_url(self, obj):
		return u'<a href="%s">Show Form</a>' % (obj.get_url())
	show_url.allow_tags = True
	show_url.short_description = 'Link'

admin.site.register(Attendee, RegistrationAdmin)
admin.site.register(Workshop, WorkshopAdmin)
