from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey, String, Text, DateTime
from datetime import datetime
from app import db


class Movie(db.Model):
    __tablename__ = 'movie'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    trailer_url: Mapped[str] = mapped_column(String(200), nullable=True)


class Cinema(db.Model):
    __tablename__ = 'cinema'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    location: Mapped[str] = mapped_column(String(200), nullable=False)


class Schedule(db.Model):
    __tablename__ = 'schedule'

    id: Mapped[int] = mapped_column(primary_key=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey('movie.id'), primary_key=True)
    cinema_id: Mapped[int] = mapped_column(ForeignKey('cinema.id'), primary_key=True)
    showtime: Mapped[datetime] = mapped_column(DateTime, nullable=False)


class Review(db.Model):
    __tablename__ = 'review'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey('movie.id'), nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    comment: Mapped[str] = mapped_column(Text, nullable=True)

