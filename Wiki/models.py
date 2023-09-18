from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=100)
    short_description = CKEditor5Field(max_length=500, verbose_name='Краткое описание', config_name='extends')
    full_description = CKEditor5Field(verbose_name='Полное описание', config_name='extends')

    def __str__(self):
        return self.name

class Child(models.Model):
    name = models.CharField(max_length=100, blank=True,)
    detail = models.CharField(max_length=1000, blank=True)
    like = models.IntegerField(default=0)
    image = models.ImageField(null=True,blank=True)
    child = models.ForeignKey(Language, on_delete=models.CASCADE)
    short_description = CKEditor5Field(max_length=500, verbose_name='Краткое описание', config_name='extends')
    full_description = CKEditor5Field(verbose_name='Полное описание', config_name='extends')

    def __str__(self):
        return self.name
