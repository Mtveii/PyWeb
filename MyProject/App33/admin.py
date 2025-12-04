from django.contrib import admin
from .models import *

# Register your models here.
# моделі, зареєстровані у даному файлі, автоматично потрапляють
# до панелі адміністратора

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name','create_level','read_level',
                    'update_level', 'delete_level')
    
admin.site.register(Role, RoleAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','last_name')
    
admin.site.register(User, UserAdmin)


class AccessAdmin(admin.ModelAdmin):
    list_display = ('login','user', 'role')

admin.site.register(Access, AccessAdmin)

# ---------дз -----------
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'access', 'status_code')
    list_filter = ('status_code', 'datetime')
    search_fields = ('access__login', 'access__user__first_name', 'access__user__last_name')
    readonly_fields = ('datetime',)
    date_hierarchy = 'datetime'

admin.site.register(AccessLog, AccessLogAdmin)
# ---------дз -----------