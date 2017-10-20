import os

import raven


SENTRY_DSN = os.environ.get('SENTRY_DSN')
SENTRY = raven.Client(SENTRY_DSN)  # pylint: disable=unused-variable
