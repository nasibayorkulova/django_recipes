from django.contrib import admin
from .models import Recipes, Categories


class RecipesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at')
    list_display_links = ('title', 'category')
    list_filter = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    # readonly_fields = ('title', 'description')


admin.site.register(Categories)
admin.site.register(Recipes, RecipesAdmin)
