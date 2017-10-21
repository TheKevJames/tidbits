import mock

from tidbits.gcloud.log import get_handler
from tidbits.gcloud.log import JsonFormatter


def test_get_handler():
    handler = get_handler()
    assert isinstance(handler.formatter, JsonFormatter)


def test_no_levelname():
    # should NOT throw a KeyError
    JsonFormatter().process_log_record({'nolevelname': 'aardvark'})
    assert True


def test_formats_for_gcloud():
    from pythonjsonlogger import jsonlogger
    m = jsonlogger.JsonFormatter.process_log_record = mock.MagicMock()

    JsonFormatter().process_log_record({'levelname': 'aardvark'})
    assert m.called_once_with({'severity': 'aardvark'})
