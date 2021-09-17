"""ChangeInstructorNameLength Migration."""

from masoniteorm.migrations import Migration


class ChangeInstructorNameLength(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("instructors") as table:
            table.string("instructor_name", 120).change()
            table.string("email", 120).change()

    def down(self):
        """
        Revert the migrations.
        """
        pass
