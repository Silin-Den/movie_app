from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import F, Sum, Max, Min, Avg
from django.views.generic import ListView


# Create your views here.
def show_all_movie(request):
    movies = Movie.objects.order_by(F('name').asc(nulls_first=True), 'rating')
    # for movie in movies:
    #     movie.save()
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'))

    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
        'total': movies.count()
    })


def show_one_movie(request, slug_movie: int):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie,
    })


class HomePageView(ListView):
    model = Movie
    template_name = 'movie_app/home.html'
    context_object_name = 'all_posts_list'
