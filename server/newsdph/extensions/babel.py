from flask import request, g, current_app
from flask_babel import Babel

babel = Babel()


@babel.localeselector
def locale():
    user = getattr(g, 'user', None)
    if user is not None:
        if request.path.startswith('/admin'):
            return 'zh_Hans_CN'
        if g.user.is_authenticated:
            return user.setting.locale or 'zh'
    return request.accept_languages.best_match(current_app.config['LANGUAGES']
                                               .keys())


@babel.timezoneselector
def timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        if g.user.is_authenticated:
            return user.setting.timezone or 'UTC'
    return 'UTC'


def init_app(app):
    babel.init_app(app)
