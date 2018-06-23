from django.shortcuts import render


def resolve_meta_tags(request):
    return {
        'image': '/static/thumbs/agulhas.jpg',
        'description': 'Find out the biggest mountains around you, and conquer them.',
        'author': 'Marcelo Tokarnia',
        'title': 'Trekkpedia',
        'url': 'https://github.com/marcelotokarnia/mountain-catalog',
        'keywords': 'Django,Vue,ApolloLinkState,SPA,Javascript,Python,Graphql'
    }


def index(request):
    return render(request, 'index.html', resolve_meta_tags(request))
