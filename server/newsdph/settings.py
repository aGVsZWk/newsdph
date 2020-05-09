import os
import sys
from sqlalchemy import create_engine

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class Operations:
    CONFIRM = 'confirm'
    RESET_PASSWORD = 'reset-password'
    CHANGE_EMAIL = 'change-email'


class CeleryConfig(object):
    broker_url = os.getenv('CELERY_BROKER_URL')
    result_backend = os.getenv('CELERY_RESULT_BACKEND')
    include = ['newsdph.tasks']
    # result_accept_content = ['json']
    # task_serializer = 'json'
    # enable_utc = True
    # task_track_started = True
    # broker_connection_max_retries = 0
    # worker_prefetch_multiplier = 1
    # worker_send_task_events = 1
    # task_reject_on_worker_lost = True
    # task_acks_late = True
    # worker_max_tasks_per_child = 10
    # broker_pool_limit = None
    # task_ignore_result = True
    # broker_transport_options = {'visibility_timeout': 86400}
    # task_default_queue = 'default'
    # task_queues = {
    #     'push': {
    #         "exchange": "push",
    #         "routing_key": "push"
    #     },
    #     'cloud': {
    #         "exchange": "cloud",
    #         "routing_key": "cloud"
    #     },
    #     'data': {
    #         "exchange": "data",
    #         "routing_key": "data"
    #     }
    # }


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 当链接关闭的时候，会自动提交

    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_FILE_UPLOADER = 'admin.upload_image'

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('Newsdph Admin', MAIL_USERNAME)

    REDIS_URL = os.getenv('REDIS_URL')

    DROPZONE_ALLOWED_FILE_TYPE = 'image'
    DROPZONE_MAX_FILE_SIZE = 3
    DROPZONE_MAX_FILES = 30
    DROPZONE_ENABLE_CSRF = True

    WHOOSHEE_MIN_STRING_LEN = 1

    VERIFY_CODE_LIFETIME = 30     # 验证码有效期
    # AVATARS_SAVE_PATH = os.path.join(ALBUMY_UPLOAD_PATH, 'avatars')
    # AVATARS_SIZE_TUPLE = (30, 100, 200)
    # MAX_CONTENT_LENGTH = 3 * 1024 * 1024  # file size exceed to 3 Mb will return a 413 error response.
    #
    # ALBUMY_ADMIN_EMAIL = os.getenv('ALBUMY_ADMIN', 'admin@helloflask.com')
    # ALBUMY_PHOTO_PER_PAGE = 12
    # ALBUMY_COMMENT_PER_PAGE = 15
    # ALBUMY_NOTIFICATION_PER_PAGE = 20
    # ALBUMY_USER_PER_PAGE = 20
    # ALBUMY_MANAGE_PHOTO_PER_PAGE = 20
    # ALBUMY_MANAGE_USER_PER_PAGE = 30
    # ALBUMY_MANAGE_TAG_PER_PAGE = 50
    # ALBUMY_MANAGE_COMMENT_PER_PAGE = 30
    # ALBUMY_SEARCH_RESULT_PER_PAGE = 20
    # ALBUMY_MAIL_SUBJECT_PREFIX = '[Albumy]'
    # ALBUMY_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    # ALBUMY_PHOTO_SIZE = {'small': 400,
    #                      'medium': 800}
    # ALBUMY_PHOTO_SUFFIX = {
    #     ALBUMY_PHOTO_SIZE['small']: '_s',  # thumbnail
    #     ALBUMY_PHOTO_SIZE['medium']: '_m',  # display
    # }

    # BLUELOG_EMAIL = os.getenv('BLUELOG_EMAIL')
    # BLUELOG_POST_PER_PAGE = 10
    # BLUELOG_MANAGE_POST_PER_PAGE = 15
    # BLUELOG_COMMENT_PER_PAGE = 15
    # # ('theme name', 'display name')
    # BLUELOG_THEMES = {'perfect_blue': 'Perfect Blue', 'black_swan': 'Black Swan'}
    # BLUELOG_SLOW_QUERY_THRESHOLD = 1
    #
    # BLUELOG_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    # BLUELOG_ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

    NEWSDPH_ADMIN_EMAIL = '2571117816@qq.com'

class DevelopmentConfig(BaseConfig):
    # SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data-dev.db')
    SQLALCHEMY_DATABASE_URI = os.getenv("MYSQL_URL")
    SQLALCHEMY_BINDS = {
        'chat': os.getenv('SQLITE_URL'),
        'live': os.getenv("POSTGRES_URL")
    }
    # session配置
    # SESSION_TYPE = "redis"
    # SESSION_REDIS = redis.StrictRedis(host=REIDS_HOST,port=REDIS_PORT)
    # SESSION_USE_SIGNER = True
    # PERMANENT_SESSION_LIFETIME = 3600*24*2 # 两天有效期，默认是秒
    # VERIFY_CODE_LIFETIME = 60     # 验证码有效期


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
