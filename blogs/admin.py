from django.contrib import admin
from .models import Category,Blog, Comment

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    list_editable = ('is_featured',)

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)

