from sqlalchemy.orm import Session
from .models import Post
from .schemas import ArticleCreate, ArticleUpdate


def create_article(db: Session, article: ArticleCreate):

    post = Post(**article.model_dump())

    db.add(post)
    db.commit()
    db.refresh(post)

    return {"status":True,"data":post}


def get_articles(db: Session, limit: int, offset: int):
    data = db.query(Post)\
         .offset(offset)\
         .limit(limit)\
         .all()

    return {"status":True,"data":data}


def get_article(db: Session, article_id: int):
    data = db.query(Post)\
             .filter(Post.id == article_id)\
             .first()

    return {"status":True,"data":data}

def update_article(db: Session, article_id: int, article: ArticleUpdate):

    post = get_article(db, article_id)

    if not post:
        return None

    for key, value in article.model_dump().items():
        setattr(post, key, value)

    db.commit()
    db.refresh(post)


    return {"status":True,"data":post}


def delete_article(db: Session, article_id: int):

    post = get_article(db, article_id)

    if not post:
        return {"status":False,"data":None}

    db.delete(post)
    db.commit()

    return {"status":True,"data":None}