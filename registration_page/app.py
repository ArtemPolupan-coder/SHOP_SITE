import flask

reg = flask.Blueprint(
    name = "reg",
    import_name = "app",
    template_folder = "registration_page/templates",
    static_folder = "registration_page/static"
)