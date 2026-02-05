from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class Product(Base):
    __tablename__ = 'products' # название таблицы в БД

    id = Column(Integer, primary_key=True, index=True) # первичный ключ
    name = Column(String, nullable=False, index=True) # название продукта (не может быть пустым)
    description = Column(Text) # описание продукта
    price = Column(Float, nullable=False) # цена (не может быть пустой)
    # внешний ключ, связывающий продукт с категорией
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    image_url = Column(String) # ссылка на изображение
    created_at = Column(DateTime, default=datetime.utcnow) # дата создания записи
    # связь с таблицей Category (продукт принадлежит одной категории)
    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}), price={self.price}>"

