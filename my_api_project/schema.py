import graphene
from graphene_django import DjangoObjectType
from core.models import Movie

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        fields = ("id", "title", "description")

class Query(graphene.ObjectType):
    all_movies = graphene.List(MovieType)

    def resolve_all_movies(root, info):
        return Movie.objects.all()

schema = graphene.Schema(query=Query)