from django.shortcuts import render
from random import randint
from mountains.models import Mountain


def resolve_meta_tags(request):
    country = request.GET.get('country')
    random = request.GET.get('random')
    if country or random:
        if country:
            queryset = Mountain.objects.filter(country__iexact=country)
        else:
            queryset = Mountain.objects.all()
        count = queryset.count()
        if count:
            random_index = randint(0, count - 1)
            mount = queryset[random_index]
            return {
                'image': ['/static/thumbs/agulhas.jpg', '/static/thumbs/jalapa.jpg'][random_index % 2],
                'description': 'Elevation: %sm' % mount.elevation,
                'author': 'Marcelo Tokarnia',
                'title': mount.name,
                'url': 'https://www.trekkpedia.com',
                'keywords': 'Django,Vue,ApolloLinkState,SPA,Javascript,Python,Graphql'
            }
    return {
        'image': '/static/thumbs/agulhas.jpg',
        'description': 'Find out the biggest mountains around you, and conquer them.',
        'author': 'Marcelo Tokarnia',
        'title': 'Trekkpedia',
        'url': 'https://www.trekkpedia.com',
        'keywords': 'Django,Vue,ApolloLinkState,SPA,Javascript,Python,Graphql'
    }


def index(request):
    return render(request, 'index.html', resolve_meta_tags(request))
