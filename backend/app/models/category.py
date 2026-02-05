from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class Category(Base):
    __tablename__ = 'categories' # название таблицы в БД

    id = Column(Integer, primary_key=True, index=True)
    # название категории (уникальное, не может быть пустым)
    name = Column(String,unique=True, nullable=False, index=True)
    # сокращенное название для URL (уникальное, не может быть пустым)
    slug = Column(String, unique=True, nullable=False, index=True)
    #  связь с таблицей Product (одна категория может содержать много продуктов)
    products = relationship("Product", backref="category")

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"


