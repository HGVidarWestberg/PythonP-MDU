#
# Fyll i funktionen animated_filter så att programmet bara
# skriver ut de animerade filmerna.
#
# Utmaning 1: Låt både animerat och komedi komma med.
# Utmaning 2: Skriv en ny funktion genre_filter(films, genre) som
# tar genren som parameter. Testa med 'skräck'.
films = [
{'title': 'Toy Story', 'genre': 'animerat'},
{'title': 'Scream', 'genre': 'skräck'},
{'title': 'Shrek', 'genre': 'animerat'},
{'title': 'Titanic', 'genre': 'drama'},
{'title': 'Frost', 'genre': 'animerat'},
{'title': 'Hundraåringen', 'genre': 'komedi'},
]
def filter(films: list, filter: str) -> list:
    result = []
    for item in films:
        if item["genre"] == filter:
            result.append(item)
    return result

animated = filter(films, "animerat")
for film in animated:
    print(f"{film['title']} ({film['genre']})")
print(f'Originallistan har fortfarande {len(films)} filmer')
