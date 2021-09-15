from masoniteorm.migrations import Migration


class CreateUsersTable(Migration):
    def up(self):
        """Run the migrations."""
        with self.schema.create("users") as table:
            table.increments("user_id")
            table.string("name")
            table.string("username").nullable()
            table.string("email").unique()
            table.string("password")
            table.string("contact").nullable()
            table.string("address").nullable()
            table.string("remember_token").nullable()
            table.timestamp("verified_at").nullable()
            table.soft_deletes()
            table.timestamps()

    def down(self):
        """Revert the migrations."""
        self.schema.drop("users")
