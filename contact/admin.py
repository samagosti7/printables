from django.contrib import admin

# Register your models here.


class NewsletterAdmin(admin.ModelAdmin):

    list_display = (
        'email', 'date',
    )
    search_fields = (
        'email', 'date',
    )
    order_by = (
        'date',
    )


class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'name', 'email', 'issue',
    )

    search_fields = (
        'name', 'email', 'issue',
    )

    order_by = (
        'date',
    )
