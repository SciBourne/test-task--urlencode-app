import inspect
import json

import pytest
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.params import Query

from test_task_urlencode.handlers import get_url_encode
from core.encode_types import EnumEncodeType
from core.encoders import URLEncoder


@pytest.mark.unit
@pytest.mark.handlers
class TestGetUrlEncode:
    DUMMY_ARGS = {
        "source": "https://yandex.ru",
        "encode_type": next(iter(EnumEncodeType))
    }

    CONTROL_RESPONSE_STATUS_CODE = status.HTTP_200_OK
    CONTROL_RESPONSE_MEDIA_TYPE = "application/json"

    CONTROL_RESPONSE_BODY = {
        "encoded_url": DUMMY_ARGS["source"],
        "encode_type": DUMMY_ARGS["encode_type"]
    }

    def test_args(self):
        args = inspect.signature(get_url_encode).parameters

        source = args.get("source").annotation.__dict__
        arg_type = source.get("__origin__")
        metadata = source.get("__metadata__")

        assert arg_type == str
        assert any([isinstance(i, Query) for i in metadata])

        encode_type = args.get("encode_type").annotation.__dict__
        arg_type = encode_type.get("__origin__")
        metadata = encode_type.get("__metadata__")

        assert arg_type == EnumEncodeType
        assert any([isinstance(i, Query) for i in metadata])

    @pytest.mark.asyncio
    async def test_response(self, monkeypatch):
        monkeypatch.setattr(
            URLEncoder,
            "encode",
            lambda *args, **kwargs: self.CONTROL_RESPONSE_BODY["encoded_url"]
        )

        response = await get_url_encode(**self.DUMMY_ARGS)
        assert isinstance(response, JSONResponse)

        assert response.status_code == self.CONTROL_RESPONSE_STATUS_CODE
        assert response.media_type == self.CONTROL_RESPONSE_MEDIA_TYPE
        assert json.loads(response.body) == self.CONTROL_RESPONSE_BODY
