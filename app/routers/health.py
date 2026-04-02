from fastapi import APIRouter

from app.services.health_service import HealthService


router = APIRouter(tags=["health"])


@router.get("/health", summary="Health check")
def health_check() -> dict[str, str]:
    return HealthService().get_status()
