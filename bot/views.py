from django.shortcuts import render
from users.models import User
from movies.models import Movie, Category, Episode
from treyler.models import Treyler



def home(request):
  user_count = User.objects.count()
  movies_count = Movie.objects.count()
  category_count = Category.objects.count()
  treyler_count = Treyler.objects.count()
  episode_count = Episode.objects.count()

  context = {
    'user_count': user_count,
    'movies_count': movies_count,
    'category_count': category_count,
    'treyler_count': treyler_count,
    'episode_count': episode_count
  }
  return render(request, "base.html", context)
