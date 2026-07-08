from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from .database import Base


class Post(Base):

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200), nullable=False)

    content = Column(Text, nullable=False)

    category = Column(String(100), nullable=False)

    status = Column(String(100), nullable=False)

    created_date = Column(
        DateTime,
        server_default=func.now()
    )

    updated_date = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )