from django.contrib import admin
from blogging.models import Post, Category
# Register your models here.

# Define an inline class here
class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
               CategoryInline,
               ]
    exclude = ('posts',)

class PostAdmin(admin.ModelAdmin):
    inlines = [
               CategoryInline,
               ]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
