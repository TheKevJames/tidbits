from tidbits.log import get_all_base_loggers
from tidbits.log import get_all_loggers


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
