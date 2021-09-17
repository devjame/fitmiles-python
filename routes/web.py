"""Web Routes."""

from masonite.routes import Delete, Get, Post, Put, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    # Instructor Route
    RouteGroup(
        [
            Get("/", "InstructorController@index").name("instructor.home"),
            # create
            Get("/create", "InstructorController@create").name("instructor.create"),
            Post("/", "InstructorController@store").name("instructor.store"),
            # show single
            Get("/@id", "InstructorController@show").name("instructor.show"),
            # Update
            Get("/@id/update", "InstructorController@edit").name("instructor.edit"),
            Put("/@id/update", "InstructorController@update").name("instructor.update"),
            # Delete
            Delete("/@id/delete", "InstructorController@destroy").name(
                "instructor.delete"
            ),
        ],
        middleware=("auth",),
        prefix="/instructor",
    ),
]

from masonite.auth import Auth

ROUTES += Auth.routes()
