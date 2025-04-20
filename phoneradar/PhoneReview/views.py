from django.shortcuts import render
from .models import Brand, PhoneModel, Review
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import PhoneModel

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'PhoneReview/brand_list.html', {'brands': brands})

def model_list(request):
    models = PhoneModel.objects.all()
    return render(request, 'PhoneReview/model_list.html', {'models': models})

def review_list(request):
    reviews = Review.objects.all().order_by('-date_published')
    return render(request, 'PhoneReview/review_list.html', {'reviews': reviews})

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    
    phones = PhoneModel.objects.all()
    return render(request, 'phonereview/add_review.html', {
        'form': form,
        'phones': phones
    })