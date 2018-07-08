import flaskWrapper


class my_project_example(flaskWrapper.fWrapper):
    def route_index(self, path, request, flaskObj):
        return "Hello"

    def route_app(self, path, request, flaskObj):
        return path


app = my_project_example()
