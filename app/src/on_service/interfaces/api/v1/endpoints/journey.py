from datetime import date
from typing import List
from fastapi import APIRouter, Query, Depends
from on_service.interfaces.api.dependencies import get_journeys_creator_use_case
from on_service.application.use_cases import JourneyCreatorUseCase
from on_service.interfaces.api.v1.schemas import JourneyReponse

router = APIRouter(prefix="/journeys")


@router.get("/search/", response_model=List[JourneyReponse])
async def get_journeys(
    from_city: str = Query(..., min_length=3, max_length=3, alias="from"),
    to_city: str = Query(..., min_length=3, max_length=3, alias="to"),
    date: date = Query(),
    journey_creator: JourneyCreatorUseCase = Depends(get_journeys_creator_use_case),
):
    result = journey_creator.create_journeys(from_city, to_city, date)
    return result
