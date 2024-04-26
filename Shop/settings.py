import flask
import os


shop_app = flask.Flask(
    import_name = "settings",
    template_folder = "Shop/templates",
    static_folder = "static",
    instance_path = os.path.abspath(__file__ + "/..")
)