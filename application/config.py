import private


ENV = 'development'
DEBUG = True
TESTING = True

STATIC_FOLDER = 'static'
TEMPLATES_FOLDER = 'templates'



SQLALCHEMY_DATABASE_URI = private.SQLALCHEMY_DATABASE_URI
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False


API_URL = 'http://ws.audioscrobbler.com/2.0/'
API_KEY = private.API_KEY


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
