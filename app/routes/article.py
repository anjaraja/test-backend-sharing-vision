from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .. import crud, schemas

router = APIRouter(prefix="/article", tags=["Article"])


@router.post("/")
def create_article(
        article: schemas.ArticleCreate,
        db: Session = Depends(get_db)
):
    return crud.create_article(db, article)


@router.get("/{limit}/{offset}")
def get_articles(
        limit: int,
        offset: int,
        db: Session = Depends(get_db)
):
    return crud.get_articles(db, limit, offset)


@router.get("/{id}")
def get_article(
        id: int,
        db: Session = Depends(get_db)
):

    article = crud.get_article(db, id)

    if not article:
        raise HTTPException(404, "Article not found")

    return article


@router.put("/{id}")
def update_article(
        id: int,
        article: schemas.ArticleUpdate,
        db: Session = Depends(get_db)
):

    result = crud.update_article(db, id, article)

    if not result:
        raise HTTPException(404, "Article not found")

    return result


@router.delete("/{id}")
def delete_article(
        id: int,
        db: Session = Depends(get_db)
):

    deleted = crud.delete_article(db, id)

    if not deleted:
        raise HTTPException(404, "Article not found")

    return {
        "message":"Deleted successfully"
    }