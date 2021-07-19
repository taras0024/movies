from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie
from .forms import ReviewForm


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


class AddReview(View):
    '''Добавить отзыв'''

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            # form.movie = movie
            form.movie_id = pk
            form.save()
        return redirect(movie.get_absolute_url())
