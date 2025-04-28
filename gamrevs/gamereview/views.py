from django.shortcuts import render, get_object_or_404
from .models import Game, Review

def game_list(request):
    games = Game.objects.all()
    return render(request, 'gamereview/gamelist.html', {'games': games})

def review_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    reviews = Review.objects.filter(game=game)
    return render(request, 'gamereview/review.html', {'game': game, 'reviews': reviews})