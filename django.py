# Log all queries
#
# Add this somewhere in settings.py:
#
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django.db.backends": {
            "handlers": [],
            "level": "DEBUG",
        },
    },
}
