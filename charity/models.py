from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import RegexValidator

# Create your models here.
# DJANGO-ORM (Object relational mapping)

#BLOG
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    count = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255, null=True)
    # category = models.ManyToManyField(Category, related_name="news_categoreis")
    author = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_by = models.CharField(max_length=255, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to="blog", null=True)
    
    # def get_absolute_url(self):
    #     return reverse("single_blog", kwargs={"pk": self.pk, "slug": self.slug})
    def __str__(self):
        return self.title+" "+str(self.created_at)+" "+str(self.updated_at)


#GALLERY
class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery", null=True)
    title = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Galleries"

#VOLUNTEER
class Volunteer(models.Model):
    g = (
        ("M", "Male"), ("F", "Female"), ("T", "Transgender")
    )
    position = models.CharField(max_length=75)
    name = models.CharField(max_length=255)    
    address = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=15, choices=g, null=True)
    email = models.CharField(max_length=100, null=True)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '98********'. Up to 10 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=10, null=True)
    joined_from = models.DateTimeField(auto_now=True)
    # slug = models.SlugField(max_length=255, null=True)

    def __str__(self):
        return self.position+" "+self.name+" "+self.address+" "+self.gender+" "+self.email+" "+self.contact+" "+str(self.joined_from)

#STATE
class State(models.Model):
    donation = models.IntegerField()
    volunteers = models.IntegerField()
    rescued = models.IntegerField()

    def __str__(self):
        return str(self.donation)+" "+str(self.volunteers)+" "+str(self.rescued)

