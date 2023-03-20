def filmEntity(item) -> dict:
    return {
        "id": str(item['_id']),
        "title": item['title'],
        "year": item['year'],
        "duration": item['duration'],
        "country": item['country'],
        "genre": item['genre'],
        "synopsis": item['synopsis']
    }

def filmsEntity(entity) -> list:
    return [filmEntity(item) for item in entity]