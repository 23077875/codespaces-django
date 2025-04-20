from django.contrib import admin
from .models import Brand, PhoneModel, Review, Resource

class PhoneModelInline(admin.TabularInline):
    model = PhoneModel
    extra = 1

class BrandAdmin(admin.ModelAdmin):
    inlines = [PhoneModelInline]
    list_display = ('name', 'origin_country', 'founded_date')
    search_fields = ('name', 'origin_country')

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class ResourceInline(admin.TabularInline):
    model = Resource
    extra = 1

class PhoneModelAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'brand', 'launch_date', 'platform')
    list_filter = ('brand', 'platform')
    inlines = [ReviewInline]

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone_model', 'author', 'rating', 'date_published')
    list_filter = ('phone_model__brand', 'rating')
    search_fields = ('title', 'content')
    inlines = [ResourceInline]

admin.site.register(Brand, BrandAdmin)
admin.site.register(PhoneModel, PhoneModelAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Resource)