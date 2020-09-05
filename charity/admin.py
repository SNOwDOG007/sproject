from django.contrib import admin
from charity.models import Blog, Gallery, Volunteer, State

# Register your models here.
# @admin.register(Blog)
class CharityAdmin(admin.ModelAdmin):
    #BLOG 
    list_display = ("title", "author", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    # readonly_fields = ("author",)

    #GALLERY
    list_display = ("image", "title")
    prepopulated_fields = {"slug": ("title",)}

    #VOLUNTEER
    list_display = ("position", "name", "address", "email", "contact")
    prepopulated_fields = {"slug": ("title",)}

    #STATE
    list_display = ("donation", "volunteers", "rescued")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Blog)
admin.site.register(Gallery)
admin.site.register(Volunteer)
admin.site.register(State)