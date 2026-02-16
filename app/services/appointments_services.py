from app.repositories.appointment_repo import find_doctorname_repo

def find_doctorname_service(db, d_id):
    result = find_doctorname_repo(db, d_id)

    if not result:
        return {
            "status": "failed",
            "message": "Requested slot is not available"
        }

    return {
        "status": "success",
        "data": result
    }
