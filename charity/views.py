from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.
#single_joinus
def SingleJoinusView(request):
    template_name = "single_joinus.html"
    return render(request, template_name)

#single_about
def SingleAboutView(request):
    template_name = "single_about.html"
    return render(request, template_name)

#single_blog
def SingleBlogView(request):
    template_name = "single_blog.html"
    return render(request, template_name)

#single_gallery
def SingleGalleryView(request):
    template_name = "single_gallery.html"
    return render(request, template_name)