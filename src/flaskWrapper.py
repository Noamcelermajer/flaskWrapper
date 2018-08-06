"""
Writen by Noam Celermajer and TechUSM
"""
import threading
import flask
import os , os.path

class fWrapper():
    def __init__(self, port=9090, host="0.0.0.0"):
        self.flaskApp = flask.Flask(self.__class__.__name__)

        @self.flaskApp.route("/", defaults={"path": "index"}, methods=["GET", "POST"])
        @self.flaskApp.route("/<path:path>", methods=["GET", "POST"])
        def allroute(path):
            root = "route_" + path.split("/")[0]
            m = getattr(self, root, self.route_404)
            return m(path, flask.request, self.flaskApp)

        self.flaskApp.run(host=host, port=port , debug=debug)

    def route_index(self, path, request, flaskObj):
        return "add this method to your class <br>def route_index(self,path, request, flaskObj):"

    def route_404(self, path, request, flaskObj):
        rsp = flask.make_response("Error: 404 Not Found", 404)
        return rsp

    def downloadFile(self, file,name):
        return flask.send_file(filename_or_fp=file,attachment_filename=name,as_attachment=True)
    def redirect(self,url):
        rsp =flask.make_response(url,303)
        rsp.headers["Location"]=url
        return rsp

    def static(self,file):
        try:
            response = flask.make_response(open(os.path.abspath(file),"rb").read())
            if file[-4:].upper() in [".PNG","JPEG",".JPG",".BMP",".TIFF",".XCF"]:
                response.headers.set('Content-Type', 'image/'+file[-4:].replace(".",""))
            return response

        except Exception as eee:
            rsp = flask.make_response("<pre>{0}</pre>".format(eee).replace(os.path.abspath(file),"."), 404)
            return rsp



