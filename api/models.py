from typing import Optional
from dataclasses import dataclass

from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import UniqueConstraint, String
from sqlalchemy.dialects.mysql import YEAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


@dataclass
class Album(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    artist: Mapped[str] = mapped_column(String(255))
    release_year: Mapped[int] = mapped_column(YEAR)
    genre: Mapped[Optional[str]] = mapped_column(String(255))
    subgenre: Mapped[Optional[str]] = mapped_column(String(255))

    __table_args__ = (
        UniqueConstraint(
            'title',
            'artist',
            'release_year',
            name='unique_title_artist_release_year'
        ),
    )

    def __repr__(self):
        return f"<Album id: {self.id}, {self.title} - {self.artist} - {self.release_year}>"  # noqa


class User(db.Model):
    username: Mapped[str] = mapped_column(String(50),
                                          primary_key=True)
    pwd_hash: Mapped[str] = mapped_column(String(255))

    def set_password(self, password):
        self.pwd_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwd_hash, password)

    def __repr__(self):
        return f"<User username:{self.username}>"
