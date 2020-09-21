from django.shortcuts import render, HttpResponse
from django.views import View
from charity.models import Volunteer

# Create your views here.
#single_joinus
def SingleJoinusView(request):
    template_name = "single_joinus.html"
    if request.method=="POST":
        post = request.POST["position"]
        uname = request.POST["name"]
        add = request.POST["address"]
        gen = request.POST["gender"]
        mail = request.POST["email"]
        contact = request.POST["contact"]

        data = Volunteer(position=post,name=uname,address=add,gender=gen,email=mail,contact=contact)
        data.save()
        res = "Dear {} Thankyou for your support".format(uname)
        return render(request,template_name,{"status":res})
        # return HttpResponse

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