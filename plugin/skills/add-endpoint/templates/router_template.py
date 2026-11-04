from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["example"])


class ExampleResponse(BaseModel):
    value: str


@router.get("/example", response_model=ExampleResponse)
def get_example() -> ExampleResponse:
    return ExampleResponse(value="Replace with the requested contract")
