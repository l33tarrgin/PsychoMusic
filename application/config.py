import private


BASE_URL = 'http://127.0.0.1:5000/'
DATABASE_URI_TEMPLATE = 'postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{db_name}'
API_URL = 'http://ws.audioscrobbler.com/2.0/'
API_KEY = private.API_KEY
SPOTIFY_CLIENT_SECRET = private.SPOTIFY_CLIENT_SECRET
SPOTIFY_CLIENT_ID = private.SPOTIFY_CLIENT_ID
SPOTIFY_REDIRECT_URI = BASE_URL + 'spotify/account'
TG_BOT_TOKEN = private.TG_BOT_TOKEN
TG_API_ID = private.TG_API_ID
TG_API_HASH_KEY = private.TG_API_HASH_KEY


class BaseConfig:
    ENV = ''
    DEBUG = True
    TESTING = True
    STATIC_FOLDER = '/static'
    TEMPLATES_FOLDER = '/templates'
    SQLALCHEMY_DATABASE_URI = DATABASE_URI_TEMPLATE.format
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'filesystem'
    SESSION_FILE_DIR = './.flask_session/'
    SECRET_KEY = private.SECRET_KEY


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = BaseConfig.SQLALCHEMY_DATABASE_URI(**private.db_properties_dev)
    pass


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = BaseConfig.SQLALCHEMY_DATABASE_URI(**private.db_properties_prod)
    pass


# PROPAGATE_EXCEPTIONS = None
# PRESERVE_CONTEXT_ON_EXCEPTION = None
# SECRET_KEY = None
# PERMANENT_SESSION_LIFETIME = None
# USE_X_SENDFILE = None
# SERVER_NAME = None
# APPLICATION_ROOT = 'app.py'
# SESSION_COOKIE_NAME = None
# SESSION_COOKIE_DOMAIN = None
# SESSION_COOKIE_PATH = None
# SESSION_COOKIE_HTTPONLY = None
# SESSION_COOKIE_SECURE = None
# SESSION_COOKIE_SAMESITE = None
# SESSION_REFRESH_EACH_REQUEST = None
# MAX_CONTENT_LENGTH = None
# SEND_FILE_MAX_AGE_DEFAULT = None
# TRAP_BAD_REQUEST_ERRORS = None
# TRAP_HTTP_EXCEPTIONS = None
# EXPLAIN_TEMPLATE_LOADING = None
# PREFERRED_URL_SCHEME = None
# JSON_AS_ASCII = None
# JSON_SORT_KEYS = None
# JSONIFY_PRETTYPRINT_REGULAR = None
# JSONIFY_MIMETYPE = None
# TEMPLATES_AUTO_RELOAD = None
# MAX_COOKIE_SIZE = None
