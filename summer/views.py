from django.shortcuts import render

def home(request):
    template_name = "index.html"
    content = {"name": "Bipin"}
    return render(request, template_name, content)