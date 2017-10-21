import logging

from tidbits.log import get_all_base_loggers
from tidbits.log import get_all_loggers
from tidbits.log import set_loglevel


def test_get_loggers():
    try:
        # implicitly imported with the first package import on py3.5+
        # importing here prevents test order from mattering
        import concurrent.futures  # pylint: disable=unused-variable
    except ImportError:
        pass

    loggers = set(get_all_loggers())
    base_loggers = set(get_all_base_loggers())

    import pip  # pylint: disable=unused-variable

    assert [x.startswith('pip') for x in set(get_all_loggers()) - loggers]
    assert set(get_all_base_loggers()) - base_loggers == {'pip'}


def test_set_loglevel_debug():
    import pip  # pylint: disable=unused-variable

    set_loglevel(debug=True)

    assert logging.getLogger().level == logging.DEBUG
    assert logging.getLogger('pip').level == logging.INFO


def test_set_loglevel_info():
    import pip  # pylint: disable=unused-variable

    set_loglevel(debug=False)

    assert logging.getLogger().level == logging.INFO
    assert logging.getLogger('pip').level == logging.WARNING
