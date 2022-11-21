class JiaError(Exception):
    def __init__(self, exc):
        self.exc = exc
        super().__init__(f"jiac error: {self.exc}")


# first implement
class create_conn:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("enter middle code")
        print(self.name)
        return self.name

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"exc_type: {exc_type}")
        print(f"exc_val: {exc_val}")
        print(f"exc_tb: {exc_tb}")
        if exc_type == JiaError:
            return True

        print("middle code exit")


# if __name__ == '__main__':
#     with create_conn("aa") as name:
#         print("middle")
#         print(f"name: {name}")
#         raise JiaError


# second implement
from contextlib import contextmanager


@contextmanager
def create_conn2(name):
    print("enter middle code")
    print(name)
    try:
        yield name
    except JiaError as e:
        print(f"e: {e}")
    finally:
        print("middle code exit")


if __name__ == '__main__':
    with create_conn2("aa") as name:
        print("middle")
        print(f"name: {name}")
        raise JiaError("fuck")
