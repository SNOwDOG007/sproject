from django.contrib import admin
from charity.models import Blog, Gallery, Volunteer, State

# Register your models here.
# @admin.register(Blog)

#django admin title/headeer
admin.site.index_title = "Charity"
admin.site.site_title = " Summer Project"
admin.site.site_header="Charity | Summer Project- Admin Panel"

#Blog
class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "content", "author", "created_at", "edited_by", "updated_at"]
    search_fields = ["title", "author"]
    list_filter = ["author", "created_at"]
    # prepopulated_fields = {"slug": ("title",)}
    # readonly_fields = ("author",)

# Gallery
class GalleryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "image"]
    # prepopulated_fields = {"slug": ("title",)}

# Volunteer
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "position", "address", "gender", "email", "contact", "joined_from"]
    search_fields = ["name", "address", "contact"]
    list_filter = ["joined_from", "gender"]
    # list_editable = ["address"]

#STATE
class StateAdmin(admin.ModelAdmin):
    list_display = ["id", "donation", "volunteers", "rescued"]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(State, StateAdmin)