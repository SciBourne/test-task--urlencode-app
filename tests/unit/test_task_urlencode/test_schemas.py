import pytest

from test_task_urlencode.schemas import ResponseURLEncode
from core.encode_types import EnumEncodeType


@pytest.mark.unit
@pytest.mark.response_schemas
class TestResponseURLEncode:
    DUMMY_URL = "https://yeandex.ru"
    DUMMY_URL = next(iter(EnumEncodeType))

    def test_pydantic_model(self):
        assert hasattr(ResponseURLEncode, "Model")
        model_attrs = ResponseURLEncode.Model.__annotations__

        assert model_attrs.get("encoded_url") == str
        assert model_attrs.get("encode_type") == EnumEncodeType

    def test_examples(self):
        assert hasattr(ResponseURLEncode, "examples")
        examples = ResponseURLEncode.examples

        assert examples.get("application/json")
        assert examples.get("application/json").get("examples")
        examples = examples.get("application/json").get("examples")

        for val in examples.values():
            assert val.get("value")
            assert val.get("value").get("encoded_url")
            assert val.get("value").get("encode_type")
