import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_api_project.settings')
django.setup()

from core.models import Movie

def populate(n=1050):
    genres = ['Action', 'Comedy', 'Drama', 'Sci-Fi', 'Horror', 'Romance']
    movies_list = [
        "The Matrix", "Inception", "Interstellar", "The Godfather", 
        "Pulp Fiction", "The Dark Knight", "Fight Club", "Forrest Gump"
    ]
    
    for i in range(n):
        title = f"{random.choice(movies_list)} {i+1}"
        description = f"This is an amazing description for movie number {i+1}. It is full of action and drama."
        release_year = random.randint(1990, 2024)
        rating = round(random.uniform(5.0, 10.0), 1)
        genre = random.choice(genres)
        
        Movie.objects.create(
            title=title,
            description=description,
            release_year=release_year,
            rating=rating,
            genre=genre
        )
    print(f"Successfully added {n} movies to the database!")

if __name__ == '__main__':
    populate()