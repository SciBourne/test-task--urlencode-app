from abc import ABC, abstractmethod

import urllib.parse
import base64

from core.encode_types import EnumEncodeType


class BaseEncoder(ABC):
    def __init__(self, url: str):
        self.__encoding: str = "utf-8"
        self.url = url

    @property
    def encoding(self) -> str:
        return self.__encoding

    @abstractmethod
    def encode(self) -> str:
        raise NotImplementedError


class Base64Encoder(BaseEncoder):
    def encode(self) -> str:
        source_bytes = bytes(self.url, self.encoding)
        encode_bytes = base64.b64encode(source_bytes)

        return encode_bytes.decode(self.encoding)


class PercentEncoder(BaseEncoder):
    def encode(self) -> str:
        return urllib.parse.quote(string=self.url, safe="")


class URLEncoder:
    def __init__(self, url: str, encode_type: EnumEncodeType):
        self._encoder: BaseEncoder

        match encode_type:
            case EnumEncodeType.base64:
                self._encoder = Base64Encoder(url)
            case EnumEncodeType.percent:
                self._encoder = PercentEncoder(url)

    def encode(self) -> str:
        return self._encoder.encode()
