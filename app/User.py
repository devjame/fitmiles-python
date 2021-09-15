"""User Model."""

from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masoniteorm.relationships import has_many


class User(Model, SoftDeletesMixin):
    """User Model."""

    __fillable__ = ["name", "email", "password"]
    __primary_key__ = "user_id"
    __force_update__ = True

    __auth__ = "email"

    @has_many("user_id", "instructor_id")
    def instrutors(self):
        from app.Instructor import Instructor

        return Instructor
