import abc
import inspect

import pytest

from core.encoders import (
    BaseEncoder,
    Base64Encoder,
    PercentEncoder,
    URLEncoder
)

from core.encode_types import EnumEncodeType


CONTROL_ENCODERS = {

    Base64Encoder: "aHR0cHM6Ly95YW5kZXgucnUvaW1hZ2VzLz9mcm9tPXRhYmJhcg==",
    PercentEncoder: "https%3A%2F%2Fyandex.ru%2Fimages%2F%3Ffrom%3Dtabbar"

}

URL = "https://yandex.ru/images/?from=tabbar"


@pytest.mark.unit
@pytest.mark.encoders
class TestBaseEncoder:
    def test_abstract_type(self):
        assert issubclass(BaseEncoder, abc.ABC)

    def test_encoding_property(self):
        assert hasattr(BaseEncoder, "encoding")
        assert isinstance(BaseEncoder.encoding, property)
        assert getattr(BaseEncoder.encoding, "fget", False)
        assert not getattr(BaseEncoder.encoding, "fset", False)

    def test_url_attribute(self):
        assert inspect.signature(BaseEncoder.__init__).parameters.get("url")

    def test_encode_abstractmethod(self):
        assert hasattr(BaseEncoder, "encode")
        assert getattr(BaseEncoder.encode, "__call__", False)
        assert getattr(BaseEncoder.encode, "__isabstractmethod__", False)


@pytest.mark.unit
@pytest.mark.encoders
class TestEncoders:
    def test_subclass(self):
        for Encoder in CONTROL_ENCODERS.keys():
            assert issubclass(Encoder, BaseEncoder)

    def test_encoding_property(self):
        for Encoder in CONTROL_ENCODERS.keys():
            assert Encoder(url=URL).encoding == "utf-8"

    def test_url_attribute(self):
        for Encoder in CONTROL_ENCODERS.keys():
            assert Encoder(url=URL).url == URL

    def test_encode_method(self):
        for Encoder in CONTROL_ENCODERS.keys():
            encoded = Encoder(url=URL).encode()

            assert isinstance(encoded, str)
            assert encoded == CONTROL_ENCODERS.get(Encoder)


@pytest.mark.unit
@pytest.mark.encoders
class TestURLEncoder:
    ENCODE_TYPE = next(iter(EnumEncodeType))

    @pytest.fixture
    def dummy_encoder(self):
        class Encoder:
            @staticmethod
            def encode():
                return self.ENCODE_TYPE

        return Encoder()

    def test__init__parameters(self):
        signature = inspect.signature(URLEncoder.__init__)

        assert signature.parameters.get("url")
        assert signature.parameters.get("encode_type")

    def test__encoder_attribute(self):
        instance = URLEncoder(url=URL, encode_type=self.ENCODE_TYPE)
        assert hasattr(instance, "_encoder")

    def test_encode_method(self, monkeypatch, dummy_encoder):
        assert hasattr(URLEncoder, "encode")

        instance = URLEncoder(url=URL, encode_type=self.ENCODE_TYPE)
        monkeypatch.setattr(instance, "_encoder", dummy_encoder)

        assert instance.encode() == self.ENCODE_TYPE
