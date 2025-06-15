from datetime import datetime
from typing import Annotated
from fastapi import APIRouter, Query
from pydantic import BaseModel, Field, constr

router = APIRouter(prefix="/journeys")


class JourneyParams(BaseModel):
    city_from: str = Field(..., alias="from")
    city_to: str = Field(..., alias="to")
    # date: datetime


@router.get("/search/")
async def get_journeys(filter_query: Annotated[JourneyParams, Query()]):
    return filter_query
