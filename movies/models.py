from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import TrigramSimilarity
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    year = models.IntegerField()
    language = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    quality = models.CharField(max_length=25)
    file_id = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=50, unique=True)

    class Meta:
        indexes = [
            GinIndex(fields=['title', 'genre', 'language', 'country', 'quality', 'code']),
        ]

    def __str__(self):
        return self.title

    def get_similarity(self, query):
        return TrigramSimilarity(self.title, query) + \
               TrigramSimilarity(self.genre, query) + \
               TrigramSimilarity(self.language, query) + \
               TrigramSimilarity(self.country, query) + \
               TrigramSimilarity(self.quality, query) + \
               TrigramSimilarity(self.code, query)
