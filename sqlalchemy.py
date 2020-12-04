# Enable logging for SQL statements:

def enable_logging():
    import logging

    logging.basicConfig()
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
