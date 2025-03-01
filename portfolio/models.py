from django.db import models
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin,HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify

class PortfolioCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
    
class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/images')
    category = models.ForeignKey(PortfolioCategory,on_delete=models.CASCADE)
    url = models.URLField(default='https://github.com/aminjoncls01?tab=repositories')
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=70)
    size = models.CharField(max_length=20, default='col-lg-5')

    def __str__(self):
        return f"{self.title} by {self.category}"

class Team(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Team/images')
    director = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True) 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.director}"

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
    
class Blog(models.Model,HitCountMixin):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Blogs/images')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=50)
    content = RichTextField()
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
    related_query_name='hit_count_generic_relation')
    slug = models.SlugField(unique=True, blank=True)  # Slug maydoni qo'shildi

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.author}"
