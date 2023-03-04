from contextlib import contextmanager


class Resource():
    def __init__(self):
        self.openned = False

    def open(self, *args):
        print(f"Resurse was opened with arguments {args}")
        self.openned = True

    def close(self):
        print(f"Resurse was closed!")
        self.openned = False

    def __del__(self):
        if self.openned:
            print("Memory leak detekted! Resurse was not closed!")

    def action(self):
        print("Do something with resourse!")


@contextmanager
def open_resource(*args):
    resource = None
    try:
        resource = Resource()
        resource.open(*args)
        yield resource
    except Exception as e:
        # log the exception
        raise  # можно использовать pass, но не рекомендуется
    finally:
        if resource:
            resource.close()
        # return True   # можно использовать, но не рекомендуется

class ResourceWorker:
    def __init__(self, *args):
        self.args = args
        self.resource = None

    def __enter__(self):
        self.resource = Resource()
        self.resource.open(*self.args)
        return self.resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.resource:
            self.resource.close()


if __name__ == "__main__":
    with ResourceWorker(1, 2, 3) as res:
        res.action()
    # with open_resource(1,2,3) as res:
    #     res.action()
    raise ValueError('Stop')
