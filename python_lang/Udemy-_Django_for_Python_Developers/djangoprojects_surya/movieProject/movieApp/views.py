from django.shortcuts import render
from movieApp.models import Movie
from movieApp.forms import MovieForm

# Create your views here.
def indexView(request):
    return render(request=request, template_name='movieApp/index.html')

def listMoviesView(request):
    moviesList = Movie.objects.all()
    return render(request=request, template_name='movieApp/listMovies.html', context={'moviesList':moviesList})

def addMovieView(request):
    movieFormData = MovieForm()
    if request.method == 'POST':
        movieForm_request_post = MovieForm(request.POST)
        if movieForm_request_post.is_valid():
            movieForm_request_post.save()
            print('MovieForm is valid')
            print('Movie Name:', movieForm_request_post.cleaned_data['name'])
            print('Movie Release Date:', str(movieForm_request_post.cleaned_data['releaseDate']))
            print('Movie Rating:', str(movieForm_request_post.cleaned_data['rating']))
        return indexView(request=request)
    return render(request=request, template_name='movieApp/addMovie.html', context={'movieForm':movieFormData})