from bs4 import BeautifulSoup
import requests

async def scrapThatFilm(url: str) -> dict:
    fUrl = f'https://www.filmaffinity.com/es/{url}.html'
    resp = requests.get(fUrl)
    soup = BeautifulSoup(resp.content, 'html.parser')
    dataFilm = soup.select('[class=movie-info]')
    
    for i in dataFilm:
        values = [value.text.strip() for value in i.find_all('dd')]
    
    filmInfo = {
        "id": "",
        "title": values[0],
        "year": values[1],
        "duration": values[2],
        "country": values[3],
        "genre": ' | '.join(' | '.join(values[10].split('.                 ')).split(' |                 ')),
        "synopsis": values[12]
    }

    return filmInfo

async def searchThatOne(query: str) -> list:
    url = f'https://www.filmaffinity.com/es/search.php?stype=title&stext={query}'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    dataFilm = soup.find_all('div', {'class': 'se-it mt'})
    cont = 0
    values = []
    for value in dataFilm:
        cont += 1
        values.append([value.find('a').attrs['title'], value.find('a').attrs['href'], cont, value.text.split('\n')[1]])
        
    return values

if __name__ == '__main__':
    #url = 'https://www.filmaffinity.com/es/film750283.html'
    q = 'el señor de los anillos'
    searchThatOne(q)
    
    #filmInf = scrapThatFilm(url)

    #print(filmInf)