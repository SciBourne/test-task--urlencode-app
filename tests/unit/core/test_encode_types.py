import pytest
from core.encode_types import EnumEncodeType


@pytest.mark.unit
@pytest.mark.encode_types
class TestEnumEncodeType:

    CONTROL_TYPES = [
        "percent",
        "base64"
    ]

    def test_presence_enum_encode_types(self):
        for etype in self.CONTROL_TYPES:
            assert etype == EnumEncodeType(etype)
            assert etype == eval(f"EnumEncodeType.{etype}")
