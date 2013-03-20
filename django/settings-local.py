DEBUG = True
# False =  DjDT is close
DEBUG_TOOLBAR = True

SECRET_KEY = 'dev_key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'ralph_dev2013-01-28',
        'NAME': 'table',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'OPTIONS': {
           "init_command": "SET storage_engine=INNODB",
        },
    },
}

CACHES = dict(
    default = dict(
        BACKEND = 'django.core.cache.backends.dummy.DummyCache',
        LOCATION = '',
        TIMEOUT = 300,
        OPTIONS = dict(
        ),
        KEY_PREFIX = 'RALPH_',
    )
)

if DEBUG_TOOLBAR is True:
    INTERNAL_IPS = ('127.0.0.1',)
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel', )
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
