import logging
import sys

from pythonjsonlogger import jsonlogger


FMT = '%(filename)s %(lineno)d %(levelname)s %(message)s %(name)s'


class JsonFormatter(jsonlogger.JsonFormatter):
    # pylint: disable=too-few-public-methods
    def __init__(self, fmt=FMT, *args, **kwargs):
        jsonlogger.JsonFormatter.__init__(self, fmt=fmt, *args, **kwargs)

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
