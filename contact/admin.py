from django.contrib import admin
from .models import Newsletter, Contact

# Register your models here.


class NewsletterAdmin(admin.ModelAdmin):

    list_display = (
        'email', 'date',
    )

    search_fields = (
        'email', 'date',
    )

    # ordering = (
    #     'date',
    # )


class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'name', 'email',
    )

    search_fields = (
        'name', 'email',
    )

    # ordering = (
    #     'date',
    # )


admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Contact, ContactAdmin)
