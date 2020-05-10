import os
from celery import Celery

import click
from flask import Flask, render_template, request
# from flask_sqlalchemy import get_debug_queries
# from bluelog.models import Admin, Post, Category, Comment, Link
from .settings import config, CeleryConfig
from .extensions import register_extensions
from .blueprints import register_blueprints
from .log import register_logging

DEFAULT_APP_NAME = 'newsdph'

def create_app(config_name):
    app_name = DEFAULT_APP_NAME
    app = Flask(app_name)
    app.config.from_object(config[config_name])
    register_logging(app)
    register_extensions(app)
    register_blueprints(app)
    # register_commands(app)
    # register_errors(app)
    # register_shell_context(app)
    # register_template_context(app)
    # register_request_handlers(app)
    return app


# def register_shell_context(app):
#     @app.shell_context_processor
#     def make_shell_context():
#         return dict(db=db, Admin=Admin, Post=Post, Category=Category, Comment=Comment)
#
#
# def register_template_context(app):
#     @app.context_processor
#     def make_template_context():
#         admin = Admin.query.first()
#         categories = Category.query.order_by(Category.name).all()
#         links = Link.query.order_by(Link.name).all()
#         if current_user.is_authenticated:
#             unread_comments = Comment.query.filter_by(reviewed=False).count()
#         else:
#             unread_comments = None
#         return dict(
#             admin=admin, categories=categories,
#             links=links, unread_comments=unread_comments)
#
#
# def register_errors(app):
#     @app.errorhandler(400)
#     def bad_request(e):
#         return render_template('errors/400.html'), 400
#
#     @app.errorhandler(404)
#     def page_not_found(e):
#         return render_template('errors/404.html'), 404
#
#     @app.errorhandler(500)
#     def internal_server_error(e):
#         return render_template('errors/500.html'), 500
#
#     @app.errorhandler(CSRFError)
#     def handle_csrf_error(e):
#         return render_template('errors/400.html', description=e.description), 400
#
#:jk
# def register_commands(app):
#     @app.cli.command()
#     @click.option('--drop', is_flag=True, help='Create after drop.')
#     def initdb(drop):
#         """Initialize the database."""
#         if drop:
#             click.confirm('This operation will delete the database, do you want to continue?', abort=True)
#             db.drop_all()
#             click.echo('Drop tables.')
#         db.create_all()
#         click.echo('Initialized database.')
#
#     @app.cli.command()
#     @click.option('--username', prompt=True, help='The username used to login.')
#     @click.option('--password', prompt=True, hide_input=True,
#                   confirmation_prompt=True, help='The password used to login.')
#     def init(username, password):
#         """Building Bluelog, just for you."""
#
#         click.echo('Initializing the database...')
#         db.create_all()
#
#         admin = Admin.query.first()
#         if admin is not None:
#             click.echo('The administrator already exists, updating...')
#             admin.username = username
#             admin.set_password(password)
#         else:
#             click.echo('Creating the temporary administrator account...')
#             admin = Admin(
#                 username=username,
#                 blog_title='Bluelog',
#                 blog_sub_title="No, I'm the real thing.",
#                 name='Admin',
#                 about='Anything about you.'
#             )
#             admin.set_password(password)
#             db.session.add(admin)
#
#         category = Category.query.first()
#         if category is None:
#             click.echo('Creating the default category...')
#             category = Category(name='Default')
#             db.session.add(category)
#
#         db.session.commit()
#         click.echo('Done.')
#
#     @app.cli.command()
#     @click.option('--category', default=10, help='Quantity of categories, default is 10.')
#     @click.option('--post', default=50, help='Quantity of posts, default is 50.')
#     @click.option('--comment', default=500, help='Quantity of comments, default is 500.')
#     def forge(category, post, comment):
#         """Generate fake data."""
#         from bluelog.fakes import fake_admin, fake_categories, fake_posts, fake_comments, fake_links
#
#         db.drop_all()
#         db.create_all()
#
#         click.echo('Generating the administrator...')
#         fake_admin()
#
#         click.echo('Generating %d categories...' % category)
#         fake_categories(category)
#
#         click.echo('Generating %d posts...' % post)
#         fake_posts(post)
#
#         click.echo('Generating %d comments...' % comment)
#         fake_comments(comment)
#
#         click.echo('Generating links...')
#         fake_links()
#
#         click.echo('Done.')
#
#
# def register_request_handlers(app):
#     @app.after_request
#     def query_profiler(response):
#         for q in get_debug_queries():
#             if q.duration >= app.config['BLUELOG_SLOW_QUERY_THRESHOLD']:
#                 app.logger.warning(
#                     'Slow query: Duration: %fs\n Context: %s\nQuery: %s\n '
#                     % (q.duration, q.context, q.statement)
#                 )
#         return response
