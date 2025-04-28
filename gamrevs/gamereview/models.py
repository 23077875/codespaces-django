from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=200)
    developer = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    cover_image = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    rating = models.IntegerField()
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.game.title} by {self.author}"