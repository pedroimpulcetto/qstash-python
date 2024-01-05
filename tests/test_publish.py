import pytest
import dotenv
from upstash_qstash import Client
from upstash_qstash.error import QstashException

QSTASH_TOKEN = dotenv.dotenv_values()["QSTASH_TOKEN"]


@pytest.fixture
def client():
    return Client(QSTASH_TOKEN)


def test_publish_to_url(client):
    res = client.publish_json(
        {
            "body": {"ex_key": "ex_value"},
            "url": "https://example.com",
            "headers": {
                "test-header": "test-value",
            },
        }
    )

    assert res["messageId"] is not None


def test_disallow_url_and_topic(client):
    with pytest.raises(QstashException):
        client.publish_json(
            {
                "url": "https://example.com",
                "topic": "test-topic",
            }
        )
