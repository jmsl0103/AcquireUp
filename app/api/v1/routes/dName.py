from fastapi import APIRouter, Depends, status, Query
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.services.appointments_services import find_doctorname_service
from app.core.database import get_db

router = APIRouter(prefix="/doctor", tags=["doctor"])


@router.get("/name")
def find_doctorname(
    d_id: int = Query(..., description="Doctor ID"),
    db: Session = Depends(get_db)
):
    response = find_doctorname_service(db, d_id)

    if response["status"] == "failed":
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=response
        )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response
    )
