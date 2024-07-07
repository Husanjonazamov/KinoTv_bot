# movies/admin.py

from django.contrib import admin
from .models import Movie, Category




class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'category', 'year', 'quality', 'language', 'country', 'code', 'file_id')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    

# Agar allaqachon ro'yxatdan o'tgan bo'lsa, qayta ro'yxatdan o'tkazishdan saqlaning
try:
    admin.site.register(Movie, MovieAdmin)
    admin.site.register(Category)
except admin.sites.AlreadyRegistered:
    pass
