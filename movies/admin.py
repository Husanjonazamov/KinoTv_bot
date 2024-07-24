# movies/admin.py

from django.contrib import admin
from .models import Movie, Category, Episode



class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1




class MovieAdmin(admin.ModelAdmin):
    inlines  = [EpisodeInline]
    list_display = ('title', 'genre', 'category', 'year', 'quality', 'language', 'country', 'code', 'file_id')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('series', 'title', 'file_id', 'episode_number', 'download_count',)




# Agar allaqachon ro'yxatdan o'tgan bo'lsa, qayta ro'yxatdan o'tkazishdan saqlaning
try:
    admin.site.register(Movie, MovieAdmin)
    admin.site.register(Category)
    admin.site.register(Episode)
except admin.sites.AlreadyRegistered:
    pass
