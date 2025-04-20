from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Brand(models.Model):
    name = models.CharField(max_length=100)
    origin_country = models.CharField(max_length=100)
    founded_date = models.DateField()
    headquarters = models.CharField(max_length=200)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class PhoneModel(models.Model):
    PLATFORM_CHOICES = [
        ('android', 'Android'),
        ('ios', 'iOS'),
        ('other', 'Other'),
    ]

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    launch_date = models.DateField()
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    specs = models.TextField(blank=True)
    image = models.ImageField(upload_to='phone_images/', blank=True)

    def __str__(self):
        return f"{self.brand.name} {self.model_name}"

class Review(models.Model):
    phone_model = models.ForeignKey(PhoneModel, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    date_published = models.DateTimeField(default=timezone.now)
    external_links = models.TextField(blank=True, help_text="Add relevant links separated by new lines")

    def __str__(self):
        return f"{self.title} - {self.phone_model}"

class Resource(models.Model):
    RESOURCE_TYPES = [
        ('video', 'Video Review'),
        ('article', 'Article'),
        ('forum', 'Forum Discussion'),
    ]

    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    url = models.URLField()
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.get_resource_type_display()} for {self.review.title}"