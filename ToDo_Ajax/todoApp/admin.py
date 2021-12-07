from django.contrib import admin
from .models import User, ToDo

# Register your models here.
class SuperAdmin(admin.ModelAdmin):
    admin.site.site_title = admin.site.site_header = 'ToDo Manager'
    list_per_page = 10

# display object name in admin table view
class UserHeader(admin.ModelAdmin):
    list_display = list_display_links = ('id', 'Name', 'Email')
    list_filter = list_display

admin.site.register(User, UserHeader)


#admin.site.register(User)
#admin.site.register(ToDo)