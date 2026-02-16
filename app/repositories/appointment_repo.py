from sqlalchemy import text
from sqlalchemy.orm import Session


def find_doctorname_repo(db: Session, d_id: int):
    sql = text("CALL find_d_name(:d_id)")

    result = db.execute(sql, {"d_id": d_id})

    doctors = []
    for row in result:
        doctors.append({
            "doctor_id": d_id,
            "doctor_name": row[0]
        })

    return doctors
