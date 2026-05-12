from __future__ import annotations

import json
from pathlib import Path
from statistics import mean
from typing import Any


class ContractService:
    def __init__(self, data: dict[str, Any]) -> None:
        self.data = data

    @classmethod
    def load(cls, data_path: Path | None = None) -> "ContractService":
        path = data_path or Path(__file__).resolve().parent.parent / "data" / "sample_contracts.json"
        return cls(json.loads(path.read_text(encoding="utf-8")))

    def agreements(self) -> list[dict[str, Any]]:
        return [self._decorate_agreement(agreement) for agreement in self.data["agreements"]]

    def obligations(self) -> list[dict[str, Any]]:
        agreements = {agreement["contractId"]: agreement for agreement in self.agreements()}
        items = []
        for obligation in self.data["obligations"]:
            agreement = agreements[obligation["contractId"]]
            items.append(
                {
                    **obligation,
                    "counterparty": agreement["counterparty"],
                    "agreementType": agreement["agreementType"],
                    "lane": agreement["lane"],
                }
            )
        return items

    def summary(self) -> dict[str, Any]:
        agreements = self.agreements()
        critical = [agreement for agreement in agreements if agreement["lane"] == "escalate"]
        watch = [agreement for agreement in agreements if agreement["lane"] == "watch"]
        return {
            "agreementCount": len(agreements),
            "criticalCount": len(critical),
            "watchCount": len(watch),
            "obligationCount": len(self.obligations()),
            "averageRiskScore": round(mean(agreement["riskScore"] for agreement in agreements), 1),
            "averageWindowDays": round(mean(agreement["obligationWindowDays"] for agreement in agreements), 1),
            "leadRecommendation": "Pull privacy, compliance, and finance blockers into a single weekly obligation review lane.",
        }

    def agreement(self, contract_id: str) -> dict[str, Any]:
        for agreement in self.agreements():
            if agreement["contractId"] == contract_id:
                return agreement
        raise KeyError(contract_id)

    def sample_payload(self) -> dict[str, Any]:
        return {
            "dashboard": self.summary(),
            "agreements": self.agreements()[:3],
            "obligations": self.obligations(),
        }

    @staticmethod
    def _decorate_agreement(agreement: dict[str, Any]) -> dict[str, Any]:
        lane = "clear"
        if agreement["riskScore"] >= 85 or agreement["obligationWindowDays"] <= 14:
            lane = "escalate"
        elif agreement["riskScore"] >= 55 or agreement["obligationWindowDays"] <= 30:
            lane = "watch"
        return {**agreement, "lane": lane}


def build_service() -> ContractService:
    return ContractService.load()
