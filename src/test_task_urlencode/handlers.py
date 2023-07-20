from typing import Annotated

from fastapi import Query, status
from fastapi.responses import JSONResponse

from fastapi_versioning import version

from core.encoders import URLEncoder
from core.encode_types import EnumEncodeType


@version(1)
async def get_url_encode(

        source: Annotated[
            str,
            Query(description="Unencoded url")
        ],

        encode_type: Annotated[
            EnumEncodeType,
            Query(description="Encode type")
        ] = EnumEncodeType.percent

) -> JSONResponse:

    encoder = URLEncoder(
        url=source,
        encode_type=encode_type
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        media_type="application/json",

        content={
            "encoded_url": encoder.encode(),
            "encode_type": encode_type
        }
    )
