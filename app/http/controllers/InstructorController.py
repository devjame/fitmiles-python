""" A InstructorController Module """

import json

from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.validation import Validator
from masonite.view import View
from app.Instructor import Instructor
from masoniteorm.exceptions import QueryException


class InstructorController(Controller):
    """Class Docstring Description"""

    def show(self, view: View, request: Request):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", InstructorController)
        """

        instructor = Instructor.find(request.param("id"))

        return view.render("instructor/single", {"instructor": instructor})

    def index(self, view: View):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", InstructorController)
        """
        instructors = Instructor.all()

        return view.render("instructor/home", {"instructors": instructors})

    def create(self, view: View):
        """Show form to create new resource listings
        ex. Get().route("/create", InstructorController)
        """

        return view.render("instructor/create")

    def store(
        self, request: Request, validate: Validator, view: View, response: Response
    ):
        """Create a new resource listing
        ex. Post target to create new Model
            Post().route("/store", InstructorController)
        """

        try:
            errors = request.validate(
                validate.required(["name", "address", "email"]),
                validate.email("email"),
            )

            if errors:
                return (
                    request.redirect_to("instructor.create")
                    .with_errors(errors)
                    .with_input()
                )

            instructor = Instructor.create(
                instructor_name=request.input("name"),
                address=request.input("address"),
                email=request.input("email"),
                user_id=request.user().user_id,
            ).fresh()

        except QueryException as e:
            error = json.dumps({"error": [str(e)]})
            return (
                request.redirect_to("instructor.create").with_errors(error).with_input()
            )

        return request.redirect_to(
            "instructor.show", {"instructor": instructor.instructor_id}
        )

    def edit(self, view: View, request: Request):
        """Show form to edit an existing resource listing
        ex. Get().route("/edit", InstructorController)
        """

        instructor = Instructor.find(request.param("id"))

        return view.render("instructor/edit", {"instructor": instructor})

    def update(self, view: View, request: Request, validate: Validator):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", InstructorController)
        """
        errors = request.validate(
            validate.required(["name", "address", "email"]),
            validate.email("email"),
        )

        if errors:
            return (
                request.redirect_to("instructor.edit").with_errors(errors).with_input()
            )

        instructor: Instructor = Instructor.find(request.param("id"))
        if not instructor:
            return request.redirect_to("instructor.home")

        instructor.instructor_name = request.input("name")
        instructor.address = request.input("address")
        instructor.email = request.input("email")
        instructor.save()

        return request.redirect_to("instructor.show", {"id": instructor.instructor_id})

    def destroy(self, request: Request):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", InstructorController)
        """

        Instructor.delete(request.param("id"))

        message = f"User with {request.param('id')} id has been deleted"

        return request.redirect_to("instructor.home").with_success(message)
