from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie


class MovieViews(ListView):
    '''Список фильмов'''

    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies/movies.html'


# class MovieDetailView(View):
#     '''Полное описание фильма'''
#
#     def get(self, request, slug):
#         movie = Movie.objects.get(url=slug)
#         return render(request, 'movies/movie_detail.html', {'movie': movie})

class MovieDetailView(DetailView):
    '''Полное описание фильма'''

    model = Movie
    slug_field = 'url'
    # template_name = <model_name>_detail
