from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AlumniUser

@admin.register(AlumniUser)
class AlumniUserAdmin(UserAdmin):
    model = AlumniUser
    list_display = ('username', 'fullname', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('fullname', 'email', 'address', 'picture')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'fullname', 'email', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'fullname', 'email')
    ordering = ('username',)
