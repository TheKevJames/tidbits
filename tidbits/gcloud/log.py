import logging
import sys

from pythonjsonlogger import jsonlogger


FMT = '%(filename)s %(lineno)d %(levelname)s %(message)s %(name)s'


class JsonFormatter(jsonlogger.JsonFormatter):
    # pylint: disable=too-few-public-methods
    def __init__(self, *args, fmt=FMT, **kwargs):
        jsonlogger.JsonFormatter.__init__(self, *args, fmt=fmt, **kwargs)

    def process_log_record(self, log_record):
        # stackdriver uses "severity" instead of "levelname"
        try:
            log_record['severity'] = log_record['levelname']
            del log_record['levelname']
        except KeyError:
            pass

        return super(JsonFormatter, self).process_log_record(log_record)


def get_handler():
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())
    return handler
