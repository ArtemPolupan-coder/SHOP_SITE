import flask

auth = flask.Blueprint(
    name = "auth",
    import_name = "app",
    template_folder = "authorization_page/templates",
    static_folder = "authorization_page/static"
)