from fastapi import APIRouter

from api.word import word_router
from api.dictionary import dictionary_router

result_router = APIRouter()

result_router.include_router(word_router)
result_router.include_router(dictionary_router)