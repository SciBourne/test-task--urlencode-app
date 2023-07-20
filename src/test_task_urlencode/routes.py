from fastapi import APIRouter, status

from test_task_urlencode import handlers
from test_task_urlencode import schemas


router = APIRouter(tags=["URL Encode"])


router.add_api_route(
    summary="Get URL-encode",
    endpoint=handlers.get_url_encode,

    methods=["GET"],
    path="/urlencode",

    status_code=status.HTTP_200_OK,
    response_model=schemas.ResponseURLEncode.Model,

    responses={
        status.HTTP_201_CREATED: {
            "model": schemas.ResponseURLEncode.Model,
            "content": schemas.ResponseURLEncode.examples
        }
    }
)
