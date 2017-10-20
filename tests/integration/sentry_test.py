import mock
import pytest


def test_requires_raven():
    with mock.patch.dict('sys.modules', {'raven': None}):
        with pytest.raises(ImportError) as e:
            from tidbits.integration.sentry import SENTRY
            _ = SENTRY

    assert e.value.message == 'No module named raven'


def test_exposes_instance():
    from tidbits.integration.sentry import SENTRY

    assert SENTRY
