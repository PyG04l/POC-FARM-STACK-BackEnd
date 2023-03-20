from fastapi import FastAPI
from routes.films import filmRoute
from docs import tags_metadata
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title='REST API FastAPI & MongoDB',
    description='Guarda las pelis vistas y marca las recomendadas',
    version='0.0.1',
    openapi_tags=tags_metadata
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(filmRoute)