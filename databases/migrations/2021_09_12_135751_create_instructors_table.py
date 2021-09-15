"""CreateInstructorsTable Migration."""

from masoniteorm.migrations import Migration


class CreateInstructorsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("instructors") as table:
            table.increments("instructor_id")
            table.string("instructor_name", 11),
            table.string("address", 100),
            table.string("email", 30),
            table.integer("user_id").unsigned()
            table.foreign("user_id").references("user_id").on("users").on_update(
                "cascade"
            )
            table.soft_deletes()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("instrutors")
