import home_page
import authorization_page
import registration_page
from .settings import shop_app

home_page.home.add_url_rule(
    rule = "/",
    view_func = home_page.render_home
)

authorization_page.auth.add_url_rule(
    rule = '/auth',
    view_func = authorization_page.render_auth
)

registration_page.reg.add_url_rule(
    rule = '/reg',
    view_func = registration_page.render_reg
)




shop_app.register_blueprint(
    blueprint = home_page.home,
)
shop_app.register_blueprint(
    blueprint = authorization_page.auth,
)
shop_app.register_blueprint(
    blueprint = registration_page.reg,
)