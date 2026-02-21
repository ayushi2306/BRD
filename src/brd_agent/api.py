from __future__ import annotations

from fastapi import FastAPI

from .builder import generate_brd
from .models import BRDRequest, BRDResponse

app = FastAPI(title="BRD Agent", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/generate", response_model=BRDResponse)
def generate(request: BRDRequest) -> BRDResponse:
    return generate_brd(request)
