Useful Python Tidbits
=====================

Ever find yourself copying and pasting small chunks of Python code between a
bunch of your projects? The goal of this library is to reduce or eliminate that
problem.

Yes, I realize that's never going to happen. Contributions are very appreciated
though, let's see how close we can get.

|pypi| |circleci| |coverage| |pythons|

Installation
------------

.. code-block:: console

    $ pip install --upgrade tidbits

Note that in an effort to keep this library generalized, optional dependencies
are not included, ie. for the `Sentry`_ integration you will still need to

.. code-block:: console

    $ pip install raven

Usage
-----

Log
~~~

Ever had to configure the loggers of all of your dependencies? This one's for
you.

.. code-block:: python

    from tidbits.log import get_all_loggers
    from tidbits.log import get_all_base_loggers
    from tidbits.log import set_loglevel

    import requests

    get_all_loggers()
    # ['requests', 'urllib3', 'urllib3.connection', 'urllib3.connectionpool', 'urllib3.poolmanager', 'urllib3.response', 'urllib3.util', 'urllib3.util.retry']

    get_all_base_loggers()
    # ['requests', 'urllib3']

    set_loglevel(debug=True)
    # sets logging.getLogger() to DEBUG and all others to INFO
    set_loglevel(debug=False)
    # sets logging.getLogger() to INFO and all others to WARNING

Integrations
~~~~~~~~~~~~

Do you use `Sentry`_? I do. And every single project I use it in contains the
same block for configuring it from the `SENTRY_DSN` environment variable.

.. code-block:: python

    from tidbits.integrations.sentry import SENTRY

    try:
        {}['missing_key']
    except Exception:
        # damn, I totally didn't expect an error here, better send it to Sentry
        SENTRY.captureException()

.. _Sentry: https://sentry.io/

.. |pypi| image:: https://img.shields.io/pypi/v/tidbits.svg?style=flat-square
    :alt: Latest PyPI Version
    :target: https://pypi.org/project/tidbits/

.. |circleci| image:: https://img.shields.io/circleci/project/github/TheKevJames/tidbits/master.svg?style=flat-square
    :alt: CircleCI Test Status
    :target: https://circleci.com/gh/TheKevJames/tidbits/tree/master

.. |coverage| image:: https://img.shields.io/codecov/c/github/thekevjames/tidbits/master.svg?style=flat-square
    :alt: Code Coverage
    :target: https://codecov.io/gh/thekevjames/tidbits

.. |pythons| image:: https://img.shields.io/pypi/pyversions/tidbits.svg?style=flat-square
    :alt: Python Version Support
    :target: https://pypi.org/project/tidbits/
