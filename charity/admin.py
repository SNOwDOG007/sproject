from django.contrib import admin
from charity.models import Blog

# Register your models here.
# @admin.register(Blog)
class CharityAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    # readonly_fields = ("author",)

admin.site.register(Blog)