from app.models import *
from django.contrib import admin

# class AddressInline(admin.StackedInline):
#     model = Address
# 
#     
# class VendorAdmin(admin.ModelAdmin):
#     # fieldsets = [
#     #     (None,               {'fields': ['question']}),
#     #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     # ]
#     # list_display = ('question', 'pub_date', 'was_published_today')
#     # list_filter = ['pub_date']
#     # search_fields = ['question']
#     # date_hierarchy = 'pub_date'
#     inlines = [AddressInline]


admin.site.register(Tag)
admin.site.register(Vendor)
admin.site.register(Property)
admin.site.register(Project)
admin.site.register(Bid)
admin.site.register(Address)