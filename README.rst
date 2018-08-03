Useful Python Tidbits
=====================

Ever find yourself copying and pasting small chunks of Python code between a
bunch of your projects? The goal of this library is to reduce or eliminate that
problem.

Yes, I realize that's never going to happen. Contributions are very appreciated
though, let's see how close we can get.

|pypi| |circleci| |pythons|

Installation
------------

.. code-block:: console

    $ pip install --upgrade tidbits

Note that in an effort to keep this library generalized, optional dependencies
are not included, ie. for the `Sentry`_ integration you will still need to

.. code-block:: console

    $ pip install raven

For convenience, these are bundled as extra dependencies, ie. you can do

.. code-block:: console

    $ pip install --upgrade tidbits[gcloud,sentry]

Usage
-----

GCloud
~~~~~~

> requires ``python-json-logger`` or ``tidbits[gcloud]``

Have you ever run an app on Google Cloud and wondered why all your logs were
marked as errors, regardless of log level? Well, most likely you weren't
formatting them correctly -- Google Cloud expects JSON logs with "severity"
rather than "levelname", which you can set with:

.. code-block:: python

    from tidbits.gcloud.log import get_handler

    logging.getLogger().addHandler(get_handler())
    # or, even better, set all your loggers at once with tidbits.log

Log
~~~

Ever had to configure the loggers of all of your dependencies? This one's for
you.

.. code-block:: python

    from tidbits.log import get_all_loggers
    from tidbits.log import get_all_base_loggers
    from tidbits.log import set_handler
    from tidbits.log import set_loglevel

    import requests

    get_all_loggers()
    # ['requests', 'urllib3', 'urllib3.connection', 'urllib3.connectionpool', 'urllib3.poolmanager', 'urllib3.response', 'urllib3.util', 'urllib3.util.retry']

    get_all_base_loggers()
    # ['requests', 'urllib3']

    set_handler(myCoolHandler, logger='applesauce')
    # the "applesauce" logger uses this (and only this) handler
    set_handler_globally(myCoolHandler)
    # all loggers use this (and only this) handler
    set_handler_globally(myCoolHandler, ignore={'aardvark', 'banana'})
    # all loggers except those listed use this (and only this) handler

    set_loglevel(debug=True)
    # sets logging.getLogger() to DEBUG and all others to INFO
    set_loglevel(debug=False)
    # sets logging.getLogger() to INFO and all others to WARNING

Integrations
~~~~~~~~~~~~

> requires ``raven`` or ``tidbits[sentry]``

Do you use `Sentry`_? I do. And every single project I use it in contains the
same block for configuring it and instrumenting the error logger.

.. code-block:: python

    from tidbits.integration.sentry import SENTRY
    from tidbits.integration.sentry import instrument_logger

    try:
        {}['missing_key']
    except Exception:
        # damn, I totally didn't expect an error here, better send it to Sentry
        SENTRY.captureException()

    # creates events in Sentry for each error log
    instrument_logger(level=logging.Error)

.. _Sentry: https://sentry.io/

.. |pypi| image:: https://img.shields.io/pypi/v/tidbits.svg?style=flat-square
    :alt: Latest PyPI Version
    :target: https://pypi.org/project/tidbits/

.. |circleci| image:: https://img.shields.io/circleci/project/github/TheKevJames/tidbits/master.svg?style=flat-square
    :alt: CircleCI Test Status
    :target: https://circleci.com/gh/TheKevJames/tidbits/tree/master

.. |pythons| image:: https://img.shields.io/pypi/pyversions/tidbits.svg?style=flat-square
    :alt: Python Version Support
    :target: https://pypi.org/project/tidbits/
