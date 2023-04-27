from django.contrib import admin
from .models import MenuItem, Menu


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent')
    list_filter = ('parent', )


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', )
    filter_horizontal = ('items', )




