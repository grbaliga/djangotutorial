from re import A
from recommender.forms import SearchForm
from django.shortcuts import render
from django.http import Http404
from .models import *
from .forms import *
import random


def find_albums(artist, from_year = None, to_year = None):
    query = Musicdata.objects.filter(artists__contains = artist)
    if from_year is not None:
        query = query.filter(year__gte = from_year)
    if to_year is not None:
        query = query.filter(year__lte = to_year)
    return list(query.order_by('-popularity').values('id','name','year'))
    

def searchform(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            from_year = None if form.cleaned_data['from_year'] == None else int(form.cleaned_data['from_year'])
            to_year = None if form.cleaned_data['to_year'] == None else int(form.cleaned_data['to_year'])
            albums = find_albums(
                    form.cleaned_data['artist'],
                    from_year,
                    to_year
                )
            
            # Random 3 of top 10 popular albums
            answer = albums[:10]
            random.shuffle(answer)
            answer = list(answer)[:3] 
            return render(request, 'recommender/searchform.html', {'form': form, 'albums': answer })
        else:
            raise Http404('Something went wrong')
    else:
        form = SearchForm()
        return render(request, 'recommender/searchform.html', {'form': form})

