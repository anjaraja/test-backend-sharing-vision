from pydantic import BaseModel, Field
from typing import Literal

class ArticleBase(BaseModel):

    title: str = Field(..., min_length=20)
    content: str = Field(..., min_length=200)
    category: str = Field(..., min_length=3)
    status: Literal["publish","draft","thrash"]


class ArticleCreate(ArticleBase):
    pass


class ArticleUpdate(ArticleBase):
    pass


class ArticleResponse(ArticleBase):
    id:int

    class Config:
        from_attributes=True