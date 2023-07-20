from enum import Enum


class EnumEncodeType(str, Enum):
    percent = "percent"
    base64 = "base64"
