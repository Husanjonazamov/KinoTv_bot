from movies.models import Category, Movie



def get_all_categories():
    return list(Category.objects.all())


def get_movies_by_category(title):
    try:
        category = Category.objects.get(title=title)
        return list(Movie.objects.filter(category=category))
    except Category.DoesNotExist:
        return []
