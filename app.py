import sys
import requests
import logging
import opentracing as ot

from flask import Flask
from flask_restplus import Api, Resource, fields
from jaeger_client import Config


app = Flask(__name__)

api = Api(app, version="1.0")


def init_jaeger_tracer(service_name=""):
    config = Config(
        config={"sampler": {"type": "const", "param": 1}, "logging": True},
        service_name="fake provider",
        validate=True,
    )
    return config.initialize_tracer()


tracer = init_jaeger_tracer("app")


@api.route("/search_site")
class SearchSite(Resource):
    @api.doc("Ping search engines")
    def put(self):
        with ot.tracer.start_span("starting pings") as ping:
            with ot.tracer.start_span("google", ping) as google:
                requests.get("http://www.google.com")
                google.set_tag("engine", "google")
            with ot.tracer.start_span("bing", ping) as bing:
                requests.get("http://www.bing.com")
                bing.set_tag("engine", "bing")
            with ot.tracer.start_span("yahoo", ping) as yahoo:
                requests.get("http://fr.yahoo.com")
                yahoo.set_tag("engine", "yahoo")


if __name__ == "__main__":
    log_level = logging.DEBUG
    logging.getLogger("").handlers = []
    logging.basicConfig(format="%(asctime)s %(message)s", level=log_level)
    port = sys.argv[1]
    app.run(host="0.0.0.0", port=port, debug=True)
