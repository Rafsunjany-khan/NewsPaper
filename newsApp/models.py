from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField

class News(models.Model):
    choice_category =(
        ('জাতীয়', 'জাতীয়'),
        ('আন্তর্জাতিক', 'আন্তর্জাতিক'),
        ('বিনোদন', 'বিনোদন'),
        ('খেলা', 'খেলা'),
    )
    title = models.CharField(max_length=800)
    category = MultiSelectField(max_length=255, choices=choice_category)
    details = RichTextUploadingField()
    date = models.DateField(default=timezone.now())
    slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
    image = models.ImageField(upload_to='NewsImage')

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    class Meta:
        verbose_name = 'ContactUs'
        verbose_name_plural = 'ContactUs'

    def __str__(self):
        """Unicode representation of ContactUs."""
        return self.name + ' / ' + str(self.phone)

class Adds(models.Model):
    name = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to='AdsImage')

    def __str__(self):
        return self.name