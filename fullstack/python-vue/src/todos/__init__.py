def main():
    """This is required for alembic migration to pick the models"""
    try:
        from todos.models import Todo  # noqa lgtm[py/unused-import]
    except Exception as e:
        print("Error occurred in migrations")
        print(e)


main()
