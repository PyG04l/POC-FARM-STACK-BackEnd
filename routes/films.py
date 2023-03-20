from fastapi import APIRouter, Response, status, Request
from config.db import conn
from schemas.film import filmEntity, filmsEntity
from models.film import Film
from middle.scrapFA import scrapThatFilm, searchThatOne
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

filmRoute = APIRouter()

@filmRoute.get('/filmSearch/{query}', response_model=list[list], tags=['films'])
async def searchOne(query: str):
    porposeList = await searchThatOne(query)
    return porposeList

@filmRoute.get('/filmScrap/{url}', response_model=Film, tags=['films'])
async def getFilmInfo(url: str):
    filmInfo = await scrapThatFilm(url)
    return filmInfo

@filmRoute.get('/films', response_model=list[Film], tags=['films'])
def getAllFilms():
    return filmsEntity(conn.local.film.find())


@filmRoute.post('/addFilm', tags=['films'])
async def addFilm(req: Request):
    reqInfo = await req.json()
    newFilm = reqInfo['body']
    #newNewFilm = await newFilm.json()
    #print(newFilm['title'])
    #newFilm = film[1]
    #print(f'NEWFILM: {newFilm}')
    #print(f'NEWFILM JSON DUMP: {json.dumps(newFilm)}')
    
    #print(newFilm[0])
    
    del newFilm['id']
    id = conn.local.film.insert_one(newFilm).inserted_id
    film = conn.local.film.find_one({'_id': id})
    return filmEntity(film)


@filmRoute.get('/films/{id}', response_model=Film, tags=['films'])
def findFilm(id: str):
    return filmEntity(conn.local.film.find_one({"_id": ObjectId(id)}))


@filmRoute.put('/films/{id}', response_model=Film, tags=['films'])
def updateFilm(id: str, film: Film):
    conn.local.film.find_one_and_update({'_id': ObjectId(id)}, {'$set': dict(film)})
    return filmEntity(conn.local.film.find_one({'_id': ObjectId(id)}))


@filmRoute.delete('/films/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['films'])
def deleteFilm(id: str):
    filmEntity(conn.local.film.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)