"""Web Routes."""

from masonite.routes import Delete, Get, Post, Put

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    # Instructor Route
    Get("/instructor", "InstructorController@index").name("instructor.home"),
    # create
    Get("/instructor/create", "InstructorController@create").name("instructor.create"),
    Post("/instructor", "InstructorController@store").name("instructor.store"),
    # show single
    Get("/instructor/@id", "InstructorController@show").name("instructor.show"),
    # Update
    Get("/instructor/@id/update", "InstructorController@edit").name("instructor.edit"),
    Put("/instructor/@id/update", "InstructorController@update").name(
        "instructor.update"
    ),
    # Delete
    Delete("/instructor/@id/delete", "InstructorController@destroy").name(
        "instructor.delete"
    ),
    #
]

from masonite.auth import Auth

ROUTES += Auth.routes()
