from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# create_engine - функция, которая создает объект engine
# settings.database_url - строка подключения к базе данных
# connect_args - дополнительные параметры подключения
engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False}, # Нужно для многопоточности
)

# Session - это как блокнот для работы с базой данных.
# sessionmaker - фабрика, которая создает эти “блокноты”
# autocommit=False - значит, что изменения не сохранятся автоматически в базу данных. Вы сами решаете, когда сохранить
# autoflush=False - SQLAlchemy не будет автоматически обновлять базу данных при каждом изменении
# bind=engine - связывает сессию с нашей базой данных (engine — это то, что мы создавали раньше)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Это основа для создания моделей в базе данных.
# declarative_base() создает базовый класс, от которого будут наследоваться все наши модели
# Все ваши модели должны наследоваться от этого класса Base
Base = declarative_base()

# Session() - создает новую сессию для работы с базой данных
# yield - это как return, но для генераторов
# finally - блок, который выполнится всегда
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

# init_db() - это специальная функция, которая создает структуру базы данных на основе наших моделей.
# Base - это базовый класс, который мы создавали ранее (наследник declarative_base())
# metadata - содержит информацию о структуре всех наших таблиц
# create_all() - метод, который создает все таблицы в базе данных
# bind=engine - указывает, с какой базой данных нужно работать
def init_db():
    Base.metadata.create_all(bind=engine)