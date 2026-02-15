from fastapi import APIRouter
router = APIRouter(prefix="/logs", tags=["logs"])


@router.get("/")
def get_logs():
    #temporary fake logs (real parser later)
    return [
        {"id": 1, "event": "Failed login", "ip": "192.168.1.10"},
        {"id": 2, "event": "Successful login", "ip": "192.168.1.10"}
    ]
    