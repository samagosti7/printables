from django.contrib import admin
from .models import Post

# Register your models here.


class BlogAdmin(admin.ModelAdmin):

    list_display = (
        'author', 'title', 'slug', 'created_on', 'description', 'status',
    )

    search_fields = (
        'author', 'title', 'slug', 'created_on', 'description', 'status',
    )


admin.site.register(Post, BlogAdmin)
