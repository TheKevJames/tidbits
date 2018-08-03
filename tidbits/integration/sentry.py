import logging

import raven
from raven.handlers.logging import SentryHandler


SENTRY = raven.Client()


def instrument_logger(logger=None, level=logging.ERROR):
    sentry = SentryHandler(SENTRY)
    sentry.setLevel(level)
    logging.getLogger(logger).addHandler(sentry)
