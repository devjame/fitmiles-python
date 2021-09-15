"""Instructor Model."""

from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masoniteorm.relationships import belongs_to


class Instructor(Model, SoftDeletesMixin):
    """Instructor Model."""

    __fillable__ = ["instructor_name", "email", "address", "email", "user_id"]
    __primary_key__ = "instructor_id"
    __force_update__ = True

    @belongs_to
    def user(self):
        from app.User import User

        return User
