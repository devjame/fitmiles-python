"""A ViewFilterProvider Service Provider."""
import pendulum

from masonite.provider import ServiceProvider
from masonite.view import View


class ViewFilterProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        pass

    def boot(self, view: View):
        """Boots services required by the container."""
        view.filter("date_format", self.date_format)

    @staticmethod
    def date_format(date):
        if isinstance(date, pendulum.DateTime):
            return date.format("YYYY-MM-DD")
        return date
