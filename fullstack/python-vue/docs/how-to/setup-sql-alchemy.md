# SQLAlchemy setup

Install `sqlalchemy`, the driver `psycopg2`, and migration tool `alembic`.

Set environment variable `SQLALCHEMY_DATABASE_URI` as below

```sh
export SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://<user>:<password>@localhost:5432/<db name>"
```

## Migrations using alembic

**To initialise**

To init alembic run `alembic init alembic` in the `src/todos` folder. Then change the

```sh
script_location = alembic
```

to

```sh
script_location = todos:alembic
```

in the `alembic.ini` file

**To generate migrations**

Edit the `env.py` file that alembic generates to update the `sqlalchemy.url`. Add the following

```py
from todos.config import SQLALCHEMY_DATABASE_URI
from todos.database import Base

# sets the database connection uri.
config.set_main_option("sqlalchemy.url", str(SQLALCHEMY_DATABASE_URI))
target_metadata = Base.metadata
```

To auto-generate the revision `PYTHONPATH=src alembic -c src/todos/alembic.ini revision --autogenerate`

To update db `PYTHONPATH=src alembic -c src/todos/alembic.ini upgrade head`
