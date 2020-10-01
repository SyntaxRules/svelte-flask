# -*- coding: utf-8 -*-
import os, sys
import random
from flask import Flask, send_from_directory

def run_web_server(debug = True):
    base_dir = '.'
    if hasattr(sys, '_MEIPASS'):
        base_dir = os.path.join(sys._MEIPASS)

    app_args = {
        "static_folder": os.path.join(base_dir, "htmlstatic"),
        "static_url_path": "",
    }
    app = Flask(__name__, **app_args)
    if debug is True:
        # Dont Cache files
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    @app.after_request
    def after_request(response):
        header = response.headers
        if debug is True:
            # Enables CORs for another site, if needed.
            # header['Access-Control-Allow-Origin'] = 'http://localhost:3000'
            """
            Add headers to both force latest IE rendering engine or Chrome Frame to not cache changes
            """
            header["Cache-Control"] = "no-cache, no-store, must-revalidate"
            header["Pragma"] = "no-cache"
            header["Expires"] = "0"
            header['Cache-Control'] = 'public, max-age=0'
        return response

    @app.route("/rand")
    def hello():
        return str(random.randint(0, 100))

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    @app.route('/<string:path>')
    def catch_all(path):
        return app.send_static_file("index.html")

    app.run(threaded=True, debug=debug)


if __name__ == "__main__":
    run_web_server()