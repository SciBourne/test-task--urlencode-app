from pydantic import BaseModel
from core.encode_types import EnumEncodeType


class ResponseURLEncode:

    class Model(BaseModel):
        encoded_url: str
        encode_type: EnumEncodeType

    examples = {
        "application/json": {
            "examples": {
                "Percent encode": {
                    "value": {
                        "encoded_url": "https%3A%2F%2Fyandex.ru",
                        "encode_type": "percent"
                    }
                },

                "Base64 encode": {
                    "value": {
                        "encoded_url": "aHR0cHM6Ly95YW5kZXgucnU=",
                        "encode_type": "base64"
                    }
                },
            }
        }
    }
