from tidbits.gcloud.log import get_handler
from tidbits.gcloud.log import JsonFormatter


def test_get_handler():
    handler = get_handler()
    assert isinstance(handler.formatter, JsonFormatter)
