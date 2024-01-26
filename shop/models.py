from django.db import models
from django.urls import reverse


# Create your models here.
class categ(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    def get_url(self):
        return reverse('cate', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class product(models.Model):
    img = models.ImageField(upload_to='product')
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    desc = models.TextField(max_length=250)
    stock = models.IntegerField()
    available = models.BooleanField()
    price = models.IntegerField()
    category = models.ForeignKey(categ, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('pro', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)


