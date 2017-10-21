import logging
import os

import raven
from raven.handlers.logging import SentryHandler


SENTRY_DSN = os.environ.get('SENTRY_DSN')
SENTRY = raven.Client(SENTRY_DSN)  # pylint: disable=unused-variable


def instrument_logger(logger=None, level=logging.ERROR):
    sentry = SentryHandler(SENTRY)
    sentry.setLevel(level)
    logging.getLogger(logger).addHandler(sentry)
