from __future__ import annotations

import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.render import render_api_summary, render_obligations, render_overview, render_queue
from app.services.contract_service import build_service

service = build_service()
app = FastAPI(
    title="Contract Obligation Command Center",
    description="Operational command center for contract obligations, milestone risk, and cross-owner escalation.",
    version="1.0.0",
)


@app.get("/", response_class=HTMLResponse)
def overview() -> str:
    return render_overview(service.summary(), service.agreements())


@app.get("/queue", response_class=HTMLResponse)
def queue() -> str:
    return render_queue(service.agreements())


@app.get("/obligations", response_class=HTMLResponse)
def obligations() -> str:
    return render_obligations(service.obligations())


@app.get("/api-summary", response_class=HTMLResponse)
def api_summary() -> str:
    return render_api_summary(service.sample_payload())


@app.get("/api/dashboard/summary")
def dashboard_summary() -> dict:
    return service.summary()


@app.get("/api/agreements")
def agreements() -> list[dict]:
    return service.agreements()


@app.get("/api/agreements/{contract_id}")
def agreement(contract_id: str) -> dict:
    return service.agreement(contract_id)


@app.get("/api/obligations")
def obligations_api() -> list[dict]:
    return service.obligations()


@app.get("/api/sample")
def sample() -> dict:
    return service.sample_payload()


def main() -> None:
    import uvicorn

    port = int(os.getenv("PORT", "4904"))
    uvicorn.run("app.main:app", host="127.0.0.1", port=port, reload=False)


if __name__ == "__main__":
    main()
