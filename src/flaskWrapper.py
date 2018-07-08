import threading

import flask


class fWrapper():
    def __init__(self, port=9090, host="0.0.0.0"):
        self.flaskApp = flask.Flask(self.__class__.__name__)

        @self.flaskApp.route("/", defaults={"path": "index"}, methods=["GET", "POST"])
        @self.flaskApp.route("/<path:path>", methods=["GET", "POST"])
        def allroute(path):
            root = "route_" + path.split("/")[0]
            m = getattr(self, root, self.route_404)
            return m(path, flask.request, self.flaskApp)

        threading.Thread(target=lambda: self.flaskApp.run(host=host, port=port)).start()

    def route_index(self, path, request, flaskObj):
        return "add this method to your class <br>def route_index(self,path, request, flaskObj):"

    def route_404(self, path, request, flaskObj):
        return "Error 404 Not Found!!!"
