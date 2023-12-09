from datetime import datetime

import pytz
from dotenv import load_dotenv
from sqlalchemy import MetaData, Table, Column, Integer, BigInteger, String, \
    Text, TIMESTAMP, ForeignKey, Boolean

load_dotenv()
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column('id', BigInteger, primary_key=True),
    Column('username', String, nullable=False),
    Column('password', String, nullable=False),
    Column(
        'last_login',
        TIMESTAMP,
        default=datetime.now(pytz.timezone('Europe/Moscow'))
    ),
    Column('first_name', String),
    Column('last_name', String),
    Column('email', String),
    Column('is_staff', Boolean, default=False),
    Column('is_superuser', Boolean, default=False),
    Column('is_active', Boolean, default=True),
    Column(
        'date_joined',
        TIMESTAMP,
        default=datetime.now(pytz.timezone('Europe/Moscow'))
    ),
)

categories = Table(
    "categories",
    metadata,
    Column('id', BigInteger, primary_key=True),
    Column('name', String),
    Column('slug', String),
)

articles = Table(
    "articles",
    metadata,
    Column('id', BigInteger, primary_key=True),
    Column('title', String, nullable=False),
    Column('text', Text, nullable=False),
    Column('slug', String),
    Column(
        'datetime',
        TIMESTAMP,
        default=datetime.now(pytz.timezone('Europe/Moscow'))
    ),
    Column('views', Integer, default=0),
    Column('author_id', BigInteger, ForeignKey('users.id')),
    Column('category_id', BigInteger, ForeignKey('categories.id')),
    # Column('tags', ),
)
