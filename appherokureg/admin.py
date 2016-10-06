from django.contrib import admin
# Register your models here.
from .models import RegForm


class RegistrationAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'company', 'role', 'email')


admin.site.register(RegForm, RegistrationAdmin)