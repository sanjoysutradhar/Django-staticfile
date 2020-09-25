from django.contrib import admin

# Register your models here.
from listings.models import listings


class listingsAdmin(admin.ModelAdmin): #Admin_field_customization
    class Meta:
        model = listings

    list_display = ['id', 'title', 'address', 'price', 'photo_main', 'realtor','is_published', ]
    list_display_links = ['id', 'title', ]
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'price',)
    list_per_page = 1


admin.site.register(listings, listingsAdmin)
